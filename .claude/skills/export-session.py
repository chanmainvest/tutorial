#!/usr/bin/env python3
"""
Export Claude Code session transcript matching /export format.

Reads the JSONL session file and produces output identical to
Claude Code's built-in /export command.

Usage: py -3 ~/.claude/skills/export-session.py [--project-dir <path>]
"""

import json
import os
import re
import sys
import subprocess
from pathlib import Path
from datetime import datetime

LINE_WIDTH = 76


def get_project_dir():
    for i, arg in enumerate(sys.argv):
        if arg == '--project-dir' and i + 1 < len(sys.argv):
            return sys.argv[i + 1]
    return os.getcwd()


def encode_project_path(project_dir):
    return ''.join(ch if ch.isalnum() else '-' for ch in project_dir)


def find_session_file(project_dir):
    claude_dir = Path.home() / '.claude' / 'projects'
    candidates = [
        encode_project_path(project_dir),
        encode_project_path(project_dir.replace('\\', '/')),
        encode_project_path(project_dir.replace('/', '\\')),
    ]
    for pv in list(candidates):
        if len(pv) > 1 and pv[1] == '-':
            candidates.append(pv[0] + pv[1:])

    for encoded in candidates:
        session_dir = claude_dir / encoded
        if session_dir.exists():
            for f in sorted(session_dir.glob('*.jsonl'),
                            key=lambda x: x.stat().st_mtime, reverse=True):
                if '.summary.' not in f.name:
                    return f

    if claude_dir.exists():
        all_f = [f for d in claude_dir.iterdir() if d.is_dir()
                 for f in d.glob('*.jsonl') if '.summary.' not in f.name]
        if all_f:
            return max(all_f, key=lambda x: x.stat().st_mtime)
    return None


def strip_xml_tags(text):
    """Remove system-reminder, local-command-caveat, and other XML wrapper tags."""
    # Remove entire system-reminder blocks
    text = re.sub(r'<system-reminder>.*?</system-reminder>\s*', '', text, flags=re.DOTALL)
    # Remove local-command-caveat blocks
    text = re.sub(r'<local-command-caveat>.*?</local-command-caveat>\s*', '', text, flags=re.DOTALL)
    # Extract content from command tags
    m = re.search(r'<command-args>(.*?)</command-args>', text, re.DOTALL)
    if m:
        # This is a slash command invocation
        cmd_name = re.search(r'<command-name>/(.*?)</command-name>', text)
        cmd_msg = re.search(r'<command-message>(.*?)</command-message>', text)
        if cmd_name:
            args = m.group(1).strip()
            return f"/{cmd_name.group(1)} {args}".strip()
    m = re.search(r'<command-name>/(.*?)</command-name>', text)
    if m and '<command-args>' not in text:
        return f"/{m.group(1)}"
    # Extract stdout from local commands
    m = re.search(r'<local-command-stdout>(.*?)</local-command-stdout>', text, re.DOTALL)
    if m:
        stdout_text = m.group(1).strip()
        remaining = re.sub(r'<local-command-stdout>.*?</local-command-stdout>', '', text, flags=re.DOTALL).strip()
        remaining = re.sub(r'<command-\w+>.*?</command-\w+>', '', remaining, flags=re.DOTALL).strip()
        if remaining:
            return remaining
        return ''  # Skip pure stdout lines
    # Remove any remaining XML tags
    text = re.sub(r'<[^>]+>', '', text)
    return text.strip()


def wrap_text(text, indent_str='  ', width=LINE_WIDTH):
    """Wrap text with indent on continuation lines."""
    lines = text.split('\n')
    result = []
    for line in lines:
        if len(line) <= width:
            result.append(line)
        else:
            # Simple word wrap
            words = line.split(' ')
            current = ''
            for word in words:
                if not current:
                    current = word
                elif len(current) + 1 + len(word) <= width:
                    current += ' ' + word
                else:
                    result.append(current)
                    current = indent_str + word
            if current:
                result.append(current)
    return '\n'.join(result)


def truncate_lines(text, max_lines=10):
    """Truncate text like /export does."""
    lines = text.split('\n')
    if len(lines) > max_lines:
        shown = '\n'.join(lines[:max_lines])
        remaining = len(lines) - max_lines
        return f"{shown}\n     \u2026 +{remaining} lines (ctrl+o to expand)"
    return text


def format_file_path(path, project_dir=None):
    """Make path relative if possible, like /export does."""
    if project_dir:
        try:
            rel = os.path.relpath(path, project_dir)
            if not rel.startswith('..'):
                return rel.replace('\\', '/')
        except ValueError:
            pass
    return path


def get_text_blocks(content):
    """Extract text from message content."""
    if isinstance(content, str):
        return [('text', content)]
    if not isinstance(content, list):
        return [('text', str(content))]

    blocks = []
    for item in content:
        if not isinstance(item, dict):
            continue
        btype = item.get('type', '')
        if btype == 'text':
            blocks.append(('text', item.get('text', '')))
        elif btype == 'tool_use':
            blocks.append(('tool_use', item))
        elif btype == 'tool_result':
            blocks.append(('tool_result', item))
    return blocks


def format_tool_name(block, project_dir=None):
    """Format tool call like /export: ToolName(args)"""
    name = block.get('name', 'unknown')
    inp = block.get('input', {})

    # Map Edit -> Update like /export does
    display_name = 'Update' if name == 'Edit' else name

    if name in ('Bash',):
        cmd = inp.get('command', '')
        if len(cmd) > 70:
            cmd = cmd[:67] + '\u2026'
        return f"{display_name}({cmd})"
    elif name in ('Read', 'Write', 'Edit'):
        fp = inp.get('file_path', '')
        fp = format_file_path(fp, project_dir)
        return f"{display_name}({fp})"
    elif name == 'Glob':
        return f"{display_name}({inp.get('pattern', '')})"
    elif name == 'Grep':
        return f"{display_name}({inp.get('pattern', '')})"
    elif name == 'Agent':
        return f"{display_name}({inp.get('description', '')})"
    elif name == 'TaskCreate':
        return f"{display_name}({inp.get('subject', '')})"
    elif name == 'TaskUpdate':
        return f"{display_name}(#{inp.get('taskId', '')})"
    elif name == 'Skill':
        return f"{display_name}({inp.get('skill', '')})"
    elif name == 'WebSearch':
        return f"{display_name}({inp.get('query', '')})"
    elif name == 'SendMessage':
        return f"{display_name}(to: {inp.get('to', '')})"
    else:
        return f"{display_name}()"


def format_tool_result_text(block):
    """Extract text from tool_result."""
    content = block.get('content', '')
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict) and item.get('type') == 'text':
                parts.append(item.get('text', ''))
        return '\n'.join(parts)
    return str(content)


def parse_session(jsonl_path, project_dir=None):
    """Parse JSONL into /export format."""
    output = []
    pending_tool_results = {}  # tool_use_id -> result text

    entries = []
    with open(jsonl_path, encoding='utf-8') as f:
        for raw_line in f:
            try:
                entries.append(json.loads(raw_line))
            except json.JSONDecodeError:
                continue

    i = 0
    while i < len(entries):
        entry = entries[i]
        entry_type = entry.get('type', '')
        message = entry.get('message', {})
        role = message.get('role', '')
        content = message.get('content', '')

        if entry_type == 'user' and role == 'user':
            blocks = get_text_blocks(content)
            user_text_parts = []
            tool_results_in_user = []

            for btype, bdata in blocks:
                if btype == 'text':
                    user_text_parts.append(bdata)
                elif btype == 'tool_result':
                    tool_results_in_user.append(bdata)

            # Process tool results that belong to previous assistant tool_use
            for tr in tool_results_in_user:
                result_text = format_tool_result_text(tr)
                if result_text.strip():
                    truncated = truncate_lines(result_text.strip(), 5)
                    indented = '\n'.join('     ' + line for line in truncated.split('\n'))
                    output.append(f"  \u23bf  {truncated.split(chr(10))[0]}")
                    if '\n' in truncated:
                        for line in truncated.split('\n')[1:]:
                            output.append(f"     {line}")
                else:
                    output.append("  \u23bf  Done")

            # Process user text
            raw_text = '\n'.join(user_text_parts).strip()
            if raw_text:
                cleaned = strip_xml_tags(raw_text)
                if cleaned:
                    wrapped = wrap_text(cleaned, '  ')
                    output.append(f"\n\u276f {wrapped}")

        elif entry_type == 'assistant' and role == 'assistant':
            blocks = get_text_blocks(content)

            # Group consecutive reads/searches
            read_count = 0
            search_count = 0

            for btype, bdata in blocks:
                if btype == 'text':
                    text = bdata.strip()
                    if text:
                        # Flush grouped reads/searches
                        if read_count > 0:
                            output.append(f"\n  Read {read_count} file{'s' if read_count > 1 else ''} (ctrl+o to expand)")
                            read_count = 0
                        if search_count > 0:
                            output.append(f"\n  Searched for {search_count} pattern{'s' if search_count > 1 else ''} (ctrl+o to expand)")
                            search_count = 0

                        wrapped = wrap_text(text, '  ')
                        output.append(f"\n\u25cf {wrapped}")

                elif btype == 'tool_use':
                    name = bdata.get('name', '')

                    # Count consecutive reads/greps for grouping
                    if name == 'Read':
                        read_count += 1
                        continue
                    elif name == 'Grep':
                        search_count += 1
                        continue

                    # Flush grouped reads/searches
                    if read_count > 0:
                        output.append(f"\n  Read {read_count} file{'s' if read_count > 1 else ''} (ctrl+o to expand)")
                        read_count = 0
                    if search_count > 0:
                        output.append(f"\n  Searched for {search_count} pattern{'s' if search_count > 1 else ''} (ctrl+o to expand)")
                        search_count = 0

                    tool_str = format_tool_name(bdata, project_dir)
                    output.append(f"\n\u25cf {tool_str}")

            # Flush remaining grouped reads/searches
            if read_count > 0:
                output.append(f"\n  Read {read_count} file{'s' if read_count > 1 else ''} (ctrl+o to expand)")
            if search_count > 0:
                output.append(f"\n  Searched for {search_count} pattern{'s' if search_count > 1 else ''} (ctrl+o to expand)")

        i += 1

    return '\n'.join(output)


def get_git_hash(project_dir):
    try:
        result = subprocess.run(
            ['git', 'log', '-1', '--format=%h'],
            capture_output=True, text=True, cwd=project_dir
        )
        return result.stdout.strip() or 'unknown'
    except Exception:
        return 'unknown'


# ---------------------------------------------------------------------------
# Token usage + cost aggregation
# ---------------------------------------------------------------------------
# USD per million tokens. Approximate published Anthropic list prices; refresh
# as needed. Unknown models leave cost as None and the report shows "unknown".
MODEL_PRICING = {
    'claude-opus-4-7':           {'in': 15.0,  'out': 75.0,  'cw': 18.75, 'cr': 1.50},
    'claude-opus-4-7[1m]':       {'in': 30.0,  'out': 150.0, 'cw': 37.50, 'cr': 3.00},
    'claude-opus-4-6':           {'in': 15.0,  'out': 75.0,  'cw': 18.75, 'cr': 1.50},
    'claude-sonnet-4-6':         {'in': 3.0,   'out': 15.0,  'cw': 3.75,  'cr': 0.30},
    'claude-sonnet-4-6-20250514':{'in': 3.0,   'out': 15.0,  'cw': 3.75,  'cr': 0.30},
    'claude-haiku-4-5':          {'in': 1.0,   'out': 5.0,   'cw': 1.25,  'cr': 0.10},
    'claude-haiku-4-5-20251001': {'in': 1.0,   'out': 5.0,   'cw': 1.25,  'cr': 0.10},
}


def _get_pricing(model_id):
    if not model_id or model_id == '<synthetic>':
        return None
    if model_id in MODEL_PRICING:
        return MODEL_PRICING[model_id]
    for known in sorted(MODEL_PRICING, key=len, reverse=True):
        if model_id.startswith(known):
            return MODEL_PRICING[known]
    return None


def _new_bucket():
    return {
        'input': 0, 'output': 0, 'cache_read': 0, 'cache_create': 0,
        'is_subagent': False,
    }


def aggregate_usage(jsonl_path):
    """Walk the JSONL once; return per-model buckets keyed by model id.

    Sub-agent (sidechain) entries are detected via `isSidechain`. If the same
    model id is used by both the main thread and sub-agents, the bucket is
    flagged so the report can label it.
    """
    per_model = {}        # model_id -> bucket
    versions = set()

    with open(jsonl_path, encoding='utf-8') as f:
        for raw in f:
            try:
                d = json.loads(raw)
            except json.JSONDecodeError:
                continue
            v = d.get('version')
            if v:
                versions.add(v)
            if d.get('type') != 'assistant':
                continue
            msg = d.get('message') or {}
            model = msg.get('model') or 'unknown'
            usage = msg.get('usage') or {}

            inp = usage.get('input_tokens', 0) or 0
            out = usage.get('output_tokens', 0) or 0
            cr = usage.get('cache_read_input_tokens', 0) or 0
            cw = usage.get('cache_creation_input_tokens', 0) or 0
            if model == '<synthetic>' and (inp + out + cr + cw) == 0:
                continue

            bucket = per_model.setdefault(model, _new_bucket())
            bucket['input'] += inp
            bucket['output'] += out
            bucket['cache_read'] += cr
            bucket['cache_create'] += cw
            if d.get('isSidechain'):
                bucket['is_subagent'] = True

    # Compute cost per model
    for model, bucket in per_model.items():
        pricing = _get_pricing(model)
        if pricing is None:
            bucket['cost'] = None
            continue
        bucket['cost'] = {
            'input':        bucket['input']        / 1_000_000 * pricing['in'],
            'output':       bucket['output']       / 1_000_000 * pricing['out'],
            'cache_read':   bucket['cache_read']   / 1_000_000 * pricing['cr'],
            'cache_create': bucket['cache_create'] / 1_000_000 * pricing['cw'],
        }
        bucket['cost']['total'] = sum(bucket['cost'].values())

    return {'per_model': per_model, 'versions': sorted(versions)}


def detect_starting_hash(jsonl_path, project_dir):
    """The git short hash that HEAD pointed to when the session began.

    The session-start `<env>` block embeds the output of `git log` as
    "Recent commits:\\n<hash> ...". We scan for that and use the top hash.
    Falls back to current HEAD if not found.
    """
    pattern = re.compile(r'Recent commits:\s*\\n([0-9a-f]{6,12})\s')
    pattern_plain = re.compile(r'Recent commits:\s*\n([0-9a-f]{6,12})\s')
    try:
        with open(jsonl_path, encoding='utf-8') as f:
            for line in f:
                if 'Recent commits:' not in line:
                    continue
                m = pattern.search(line) or pattern_plain.search(line)
                if m:
                    return m.group(1)
    except Exception:
        pass
    return get_git_hash(project_dir)


def _fmt_money(x):
    if x is None:
        return 'unknown'
    if x and x < 0.01:
        return f"${x:.4f}"
    return f"${x:.2f}"


def format_metadata_header(usage_info, agent_version, starting_hash):
    fmt = lambda n: f"{n:,}"
    per_model = usage_info['per_model']

    main_models = sorted(m for m, b in per_model.items() if not b['is_subagent'])
    sub_models  = sorted(m for m, b in per_model.items() if b['is_subagent'])

    grand = {'input': 0, 'output': 0, 'cache_read': 0, 'cache_create': 0}
    grand_cost = 0.0
    grand_cost_known = True
    for b in per_model.values():
        for k in grand:
            grand[k] += b[k]
        if b.get('cost') is None:
            grand_cost_known = False
        else:
            grand_cost += b['cost']['total']
    grand_total_tokens = sum(grand.values())

    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    lines = [
        '=== Session Metadata ===',
        f"Agent:            {agent_version}",
        f"Model(s):         {', '.join(main_models) or 'unknown'}",
        f"Sub-agent models: {', '.join(sub_models) or 'none'}",
        f"Started from:     {starting_hash}",
        f"Date:             {now}",
        '',
        'Per-model usage and cost (sub-agent calls included):',
    ]

    for model in sorted(per_model):
        b = per_model[model]
        label = model + ('  [sub-agent]' if b['is_subagent'] else '')
        cost = b.get('cost')
        lines.append(f"  -- {label} --")
        lines.append(f"     Input tokens:        {fmt(b['input'])}    {_fmt_money(cost['input'] if cost else None)}")
        lines.append(f"     Output tokens:       {fmt(b['output'])}    {_fmt_money(cost['output'] if cost else None)}")
        lines.append(f"     Cache read tokens:   {fmt(b['cache_read'])}    {_fmt_money(cost['cache_read'] if cost else None)}")
        lines.append(f"     Cache write tokens:  {fmt(b['cache_create'])}    {_fmt_money(cost['cache_create'] if cost else None)}")
        sub_total_tokens = b['input'] + b['output'] + b['cache_read'] + b['cache_create']
        lines.append(f"     Subtotal:            {fmt(sub_total_tokens)} tokens    {_fmt_money(cost['total'] if cost else None)}")
        lines.append('')

    lines += [
        'Grand total (all models, all sub-agents):',
        f"  Input tokens:        {fmt(grand['input'])}",
        f"  Output tokens:       {fmt(grand['output'])}",
        f"  Cache read tokens:   {fmt(grand['cache_read'])}",
        f"  Cache write tokens:  {fmt(grand['cache_create'])}",
        f"  Total tokens:        {fmt(grand_total_tokens)}",
        f"  Total cost (USD):    " + (_fmt_money(grand_cost) if grand_cost_known else f"{_fmt_money(grand_cost)} (partial - one or more models missing from MODEL_PRICING)"),
        '========================',
        '',
    ]
    return '\n'.join(lines)


def main():
    project_dir = get_project_dir()
    print(f"Project: {project_dir}")

    session_file = find_session_file(project_dir)
    if not session_file:
        print("ERROR: Could not find session JSONL file")
        sys.exit(1)

    print(f"Session: {session_file.name}")

    transcript = parse_session(session_file, project_dir)

    usage_info = aggregate_usage(session_file)
    starting_hash = detect_starting_hash(session_file, project_dir)
    agent_version = (
        f"Claude Code v{usage_info['versions'][-1]}"
        if usage_info['versions'] else 'Claude Code (version unknown)'
    )
    header = format_metadata_header(usage_info, agent_version, starting_hash)

    today = datetime.now().strftime('%Y-%m-%d')
    output_dir = os.path.join(project_dir, 'session_history')
    os.makedirs(output_dir, exist_ok=True)

    # Filename uses the *starting* hash (per CLAUDE.md spec), not current HEAD.
    base_name = f"{today}_from_{starting_hash}"
    output_path = os.path.join(output_dir, f"{base_name}.log")
    counter = 2
    while os.path.exists(output_path):
        output_path = os.path.join(output_dir, f"{base_name}_{counter}.log")
        counter += 1

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(header)
        f.write(transcript)

    print(f"Exported: {output_path}")
    print(f"Size: {os.path.getsize(output_path):,} bytes")
    print(f"Started from: {starting_hash}")
    print(f"Models: {', '.join(usage_info['per_model'].keys()) or 'unknown'}")


if __name__ == '__main__':
    main()
