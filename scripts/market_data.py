"""Real-data fetcher and local cache for the tutorial course.

Lessons import this module to obtain real historical market data
(FRED, Yahoo Finance, Stooq, Damodaran). Data is cached locally so
chart-generation scripts run quickly and reproducibly without
re-downloading on every render.

Cache directory: scripts/.market_data_cache/
Cache format: gzipped CSV (works without pyarrow). Refresh window: 7 days.

Public functions:
    fred_series(series_id, start=None, end=None) -> pd.DataFrame
    yahoo_history(ticker, start="1970-01-01", end=None, interval="1d") -> pd.DataFrame
    stooq_history(symbol) -> pd.DataFrame
    damodaran_annual_returns() -> pd.DataFrame   # offline-safe
    cache_path(key) -> Path

CLI:
    python scripts/market_data.py prefetch       # populate common series
    python scripts/market_data.py info           # list cache contents

The module is dependency-light: pandas + requests (or urllib fallback).
"""

from __future__ import annotations

import gzip
import io
import json
import os
import sys
import time
from pathlib import Path
from typing import Optional
from urllib.parse import quote

import pandas as pd

try:
    import requests
    _HAS_REQUESTS = True
except ImportError:
    import urllib.request
    _HAS_REQUESTS = False


CACHE_DIR = Path(__file__).resolve().parent / ".market_data_cache"
CACHE_DIR.mkdir(exist_ok=True)
DEFAULT_TTL_SECONDS = 7 * 24 * 3600  # 7 days

USER_AGENT = "chanmainvest-tutorial/1.0 (+https://chanmainvest.github.io/tutorial/)"


def cache_path(key: str) -> Path:
    safe = key.replace("/", "_").replace("?", "_").replace("&", "_").replace("=", "_")
    return CACHE_DIR / f"{safe}.csv.gz"


def _cache_fresh(p: Path, ttl: int = DEFAULT_TTL_SECONDS) -> bool:
    if not p.exists():
        return False
    return (time.time() - p.stat().st_mtime) < ttl


def _http_get(url: str, timeout: int = 30) -> bytes:
    if _HAS_REQUESTS:
        r = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=timeout)
        r.raise_for_status()
        return r.content
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def _save_df(df: pd.DataFrame, p: Path) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(p, "wt", encoding="utf-8", newline="") as f:
        df.to_csv(f, index=True)


def _load_df(p: Path) -> pd.DataFrame:
    with gzip.open(p, "rt", encoding="utf-8") as f:
        df = pd.read_csv(f, index_col=0, parse_dates=[0])
    return df


# ---------------------------------------------------------------------------
# FRED (Federal Reserve Economic Data) — public CSV endpoint, no API key.
# ---------------------------------------------------------------------------

def fred_series(
    series_id: str,
    start: Optional[str] = None,
    end: Optional[str] = None,
    refresh: bool = False,
) -> pd.DataFrame:
    """Fetch a FRED series as a single-column DataFrame indexed by date.

    Uses the public fredgraph.csv endpoint (no API key required).
    """
    p = cache_path(f"fred_{series_id}")
    if not refresh and _cache_fresh(p):
        df = _load_df(p)
    else:
        url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
        try:
            raw = _http_get(url)
            df = pd.read_csv(io.BytesIO(raw))
            # FRED schema: DATE, <series_id>
            date_col = df.columns[0]
            val_col = df.columns[1]
            df[val_col] = pd.to_numeric(df[val_col], errors="coerce")
            df = df.dropna(subset=[val_col])
            df[date_col] = pd.to_datetime(df[date_col])
            df = df.set_index(date_col)
            df.columns = [series_id]
            _save_df(df, p)
        except Exception as e:
            if p.exists():
                df = _load_df(p)
            else:
                raise RuntimeError(f"FRED fetch failed for {series_id}: {e}")

    if start:
        df = df[df.index >= pd.to_datetime(start)]
    if end:
        df = df[df.index <= pd.to_datetime(end)]
    return df


# ---------------------------------------------------------------------------
# Yahoo Finance — chart API JSON. (CSV download was deprecated.)
# ---------------------------------------------------------------------------

def yahoo_history(
    ticker: str,
    start: str = "1970-01-01",
    end: Optional[str] = None,
    interval: str = "1d",
    refresh: bool = False,
) -> pd.DataFrame:
    """Fetch Yahoo Finance OHLCV history for a ticker.

    Returns DataFrame with columns: Open, High, Low, Close, AdjClose, Volume.
    """
    p = cache_path(f"yahoo_{ticker}_{interval}")
    if not refresh and _cache_fresh(p):
        return _filter_dates(_load_df(p), start, end)

    period1 = int(pd.Timestamp(start).timestamp())
    period2 = int(pd.Timestamp(end).timestamp()) if end else int(time.time())
    url = (
        f"https://query1.finance.yahoo.com/v8/finance/chart/{quote(ticker)}"
        f"?period1={period1}&period2={period2}&interval={interval}"
        f"&events=history&includeAdjustedClose=true"
    )
    try:
        raw = _http_get(url)
        data = json.loads(raw)
        result = data["chart"]["result"][0]
        ts = result["timestamp"]
        ind = result["indicators"]
        quote_data = ind["quote"][0]
        adj = ind.get("adjclose", [{}])[0].get("adjclose", quote_data["close"])
        df = pd.DataFrame(
            {
                "Open": quote_data["open"],
                "High": quote_data["high"],
                "Low": quote_data["low"],
                "Close": quote_data["close"],
                "AdjClose": adj,
                "Volume": quote_data["volume"],
            },
            index=pd.to_datetime(ts, unit="s").normalize(),
        ).dropna(how="all")
        _save_df(df, p)
        return _filter_dates(df, start, end)
    except Exception as e:
        if p.exists():
            return _filter_dates(_load_df(p), start, end)
        raise RuntimeError(f"Yahoo fetch failed for {ticker}: {e}")


def _filter_dates(df: pd.DataFrame, start, end) -> pd.DataFrame:
    if start:
        df = df[df.index >= pd.to_datetime(start)]
    if end:
        df = df[df.index <= pd.to_datetime(end)]
    return df


# ---------------------------------------------------------------------------
# Stooq — fallback for Yahoo, especially handy for non-US tickers.
# ---------------------------------------------------------------------------

def stooq_history(symbol: str, refresh: bool = False) -> pd.DataFrame:
    """Stooq daily CSV. Symbols are lowercase, e.g. 'spx', 'tsm.us', 'gld.us'."""
    p = cache_path(f"stooq_{symbol}")
    if not refresh and _cache_fresh(p):
        return _load_df(p)
    url = f"https://stooq.com/q/d/l/?s={symbol}&i=d"
    try:
        raw = _http_get(url)
        df = pd.read_csv(io.BytesIO(raw))
        if df.empty or "Date" not in df.columns:
            raise RuntimeError("empty stooq response")
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.set_index("Date").sort_index()
        _save_df(df, p)
        return df
    except Exception as e:
        if p.exists():
            return _load_df(p)
        raise RuntimeError(f"Stooq fetch failed for {symbol}: {e}")


# ---------------------------------------------------------------------------
# Damodaran annual return dataset — embedded offline copy so charts always
# render even when the NYU page is unreachable. Source:
#   https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html
# Updated through 2024 (most recent confirmed annual print at time of writing).
# ---------------------------------------------------------------------------

# Year, S&P500_total_return, T_bill_3m, T_bond_10y, BAA_corp_bond, CPI_yoy
# Source: Damodaran annual histretSP table (decimal). Light additions for 2023-2024.
_DAMODARAN_CSV = """Year,SP500,TBill3M,TBond10Y,BAACorp,CPI
1928,0.4381,0.0308,0.0084,0.0397,-0.0117
1929,-0.0830,0.0316,0.0420,0.0322,0.0058
1930,-0.2512,0.0455,0.0454,0.0719,-0.0640
1931,-0.4384,0.0231,-0.0256,-0.0466,-0.0932
1932,-0.0864,0.0107,0.0879,0.1051,-0.1027
1933,0.4998,0.0096,0.0186,0.2191,0.0076
1934,-0.0119,0.0032,0.0796,0.1399,0.0152
1935,0.4674,0.0018,0.0447,0.1110,0.0299
1936,0.3194,0.0017,0.0502,0.0866,0.0145
1937,-0.3534,0.0030,0.0138,-0.0116,0.0286
1938,0.2928,0.0008,0.0421,0.0855,-0.0278
1939,-0.0110,0.0004,0.0441,0.0428,-0.0048
1940,-0.1067,0.0003,0.0540,0.0411,0.0096
1941,-0.1277,0.0008,-0.0202,0.0247,0.0972
1942,0.1917,0.0034,0.0229,0.0287,0.0929
1943,0.2506,0.0038,0.0249,0.0497,0.0316
1944,0.1903,0.0038,0.0258,0.0473,0.0211
1945,0.3582,0.0038,0.0380,0.0395,0.0225
1946,-0.0843,0.0038,0.0313,0.0157,0.1817
1947,0.0520,0.0058,0.0092,-0.0047,0.0901
1948,0.0570,0.0104,0.0195,0.0376,0.0271
1949,0.1830,0.0110,0.0466,0.0759,-0.0180
1950,0.3081,0.0120,0.0043,0.0234,0.0579
1951,0.2368,0.0149,-0.0030,-0.0179,0.0587
1952,0.1815,0.0166,0.0227,0.0344,0.0088
1953,-0.0121,0.0182,0.0414,0.0345,0.0062
1954,0.5256,0.0086,0.0329,0.0660,-0.0050
1955,0.3260,0.0157,-0.0134,0.0008,0.0037
1956,0.0744,0.0246,-0.0226,-0.0218,0.0286
1957,-0.1046,0.0314,0.0680,0.0739,0.0302
1958,0.4372,0.0154,-0.0210,-0.0259,0.0176
1959,0.1206,0.0295,-0.0265,0.0112,0.0150
1960,0.0034,0.0266,0.1164,0.0907,0.0148
1961,0.2664,0.0213,0.0206,0.0482,0.0067
1962,-0.0881,0.0273,0.0564,0.0795,0.0122
1963,0.2280,0.0312,0.0181,0.0319,0.0165
1964,0.1648,0.0354,0.0383,0.0476,0.0119
1965,0.1245,0.0393,0.0069,-0.0046,0.0192
1966,-0.1006,0.0476,0.0299,0.0020,0.0335
1967,0.2398,0.0421,-0.0172,-0.0495,0.0304
1968,0.1106,0.0521,0.0298,0.0257,0.0472
1969,-0.0850,0.0658,-0.0509,-0.0809,0.0611
1970,0.0386,0.0653,0.1875,0.1837,0.0549
1971,0.1430,0.0439,0.1387,0.1101,0.0336
1972,0.1899,0.0384,0.0369,0.0726,0.0341
1973,-0.1469,0.0693,0.0179,0.0114,0.0880
1974,-0.2647,0.0800,0.0369,-0.0306,0.1220
1975,0.3723,0.0580,0.0218,0.1464,0.0701
1976,0.2393,0.0508,0.1364,0.1865,0.0481
1977,-0.0716,0.0512,0.0069,0.0139,0.0677
1978,0.0657,0.0718,-0.0118,0.0151,0.0903
1979,0.1861,0.1038,-0.0123,-0.0042,0.1331
1980,0.3250,0.1124,-0.0304,-0.0251,0.1240
1981,-0.0492,0.1471,0.0823,0.0962,0.0894
1982,0.2155,0.1054,0.3281,0.4256,0.0387
1983,0.2256,0.0880,0.0320,0.0625,0.0380
1984,0.0627,0.0985,0.1373,0.1660,0.0395
1985,0.3173,0.0772,0.2571,0.3050,0.0377
1986,0.1867,0.0616,0.2428,0.1993,0.0113
1987,0.0525,0.0547,-0.0496,-0.0056,0.0441
1988,0.1661,0.0635,0.0822,0.1570,0.0442
1989,0.3169,0.0837,0.1769,0.1836,0.0465
1990,-0.0310,0.0781,0.0624,0.0689,0.0611
1991,0.3047,0.0560,0.1500,0.2168,0.0306
1992,0.0762,0.0351,0.0936,0.1019,0.0290
1993,0.1008,0.0290,0.1421,0.1747,0.0275
1994,0.0132,0.0390,-0.0804,-0.0285,0.0267
1995,0.3758,0.0560,0.2348,0.2274,0.0254
1996,0.2296,0.0521,0.0143,0.0331,0.0332
1997,0.3336,0.0526,0.0994,0.1213,0.0170
1998,0.2858,0.0486,0.1492,0.0676,0.0161
1999,0.2104,0.0468,-0.0825,-0.0710,0.0268
2000,-0.0910,0.0589,0.1666,0.0962,0.0339
2001,-0.1189,0.0383,0.0557,0.1066,0.0155
2002,-0.2210,0.0165,0.1512,0.0899,0.0238
2003,0.2868,0.0102,0.0038,0.1709,0.0188
2004,0.1088,0.0120,0.0449,0.0768,0.0326
2005,0.0491,0.0298,0.0287,0.0265,0.0342
2006,0.1579,0.0479,0.0196,0.0586,0.0254
2007,0.0549,0.0466,0.1021,0.0387,0.0408
2008,-0.3700,0.0160,0.2010,-0.0521,0.0009
2009,0.2646,0.0010,-0.1112,0.2335,0.0272
2010,0.1506,0.0012,0.0846,0.1352,0.0150
2011,0.0211,0.0004,0.1604,0.0717,0.0296
2012,0.1600,0.0006,0.0297,0.1023,0.0174
2013,0.3239,0.0002,-0.0910,-0.0193,0.0150
2014,0.1369,0.0002,0.1075,0.1037,0.0076
2015,0.0138,0.0002,0.0128,-0.0530,0.0073
2016,0.1196,0.0020,0.0069,0.1071,0.0207
2017,0.2183,0.0080,0.0280,0.0946,0.0211
2018,-0.0438,0.0193,-0.0002,-0.0227,0.0191
2019,0.3149,0.0206,0.0964,0.1485,0.0229
2020,0.1840,0.0036,0.1133,0.0975,0.0136
2021,0.2871,0.0006,-0.0442,-0.0090,0.0703
2022,-0.1811,0.0202,-0.1777,-0.1466,0.0645
2023,0.2629,0.0511,0.0303,0.0855,0.0341
2024,0.2502,0.0495,-0.0170,0.0480,0.0289
"""


def damodaran_annual_returns() -> pd.DataFrame:
    """Annual US asset class returns (Damodaran). Columns are decimals."""
    df = pd.read_csv(io.StringIO(_DAMODARAN_CSV))
    df["Year"] = df["Year"].astype(int)
    return df.set_index("Year")


# ---------------------------------------------------------------------------
# Curated prefetch list. Run `python market_data.py prefetch` to warm cache.
# ---------------------------------------------------------------------------

PREFETCH_FRED = [
    "CPIAUCSL", "M2SL", "GFDEBTN", "DGS10", "DGS2", "DGS3MO",
    "FEDFUNDS", "UNRATE", "T10YIE", "BAMLH0A0HYM2",
    "GOLDAMGBD228NLBM", "DCOILWTICO", "VIXCLS", "DTWEXBGS",
    "GS10", "TB3MS", "AAA", "BAA", "MORTGAGE30US",
]

PREFETCH_YAHOO = [
    "^GSPC", "^DJI", "^IXIC", "^RUT", "^VIX", "^VVIX", "^TNX",
    "GLD", "SLV", "TLT", "IEF", "SHY", "AGG", "BND",
    "VTI", "VXUS", "EEM", "EFA", "QQQ", "SPY", "VOO",
    "USO", "UUP", "FXE", "FXY", "BTC-USD",
    "TSM", "AAPL", "MSFT", "NVDA", "GOOGL", "META", "AMZN",
]


def prefetch(verbose: bool = True) -> None:
    """Warm the cache for the curated common-series list."""
    fails = []
    for sid in PREFETCH_FRED:
        try:
            n = len(fred_series(sid, refresh=True))
            if verbose:
                print(f"  FRED  {sid:<22}  rows={n}")
        except Exception as e:
            fails.append(("FRED", sid, str(e)))
            if verbose:
                print(f"  FRED  {sid:<22}  FAIL: {e}")
    for ticker in PREFETCH_YAHOO:
        try:
            n = len(yahoo_history(ticker, refresh=True))
            if verbose:
                print(f"  YHOO  {ticker:<22}  rows={n}")
        except Exception as e:
            fails.append(("YAHOO", ticker, str(e)))
            if verbose:
                print(f"  YHOO  {ticker:<22}  FAIL: {e}")
    if fails:
        print(f"\n{len(fails)} failures:")
        for src, sid, err in fails:
            print(f"  {src} {sid}: {err}")


def info() -> None:
    files = sorted(CACHE_DIR.glob("*.csv.gz"))
    total = 0
    for f in files:
        sz = f.stat().st_size
        total += sz
        age = (time.time() - f.stat().st_mtime) / 86400
        print(f"  {f.name:<48}  {sz/1024:>8.1f} KB   {age:>5.1f}d old")
    print(f"\n  {len(files)} files, {total/1024:.1f} KB total")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "info"
    if cmd == "prefetch":
        prefetch()
    elif cmd == "info":
        info()
    else:
        print(f"unknown command: {cmd}")
        print("usage: python market_data.py {prefetch|info}")
        sys.exit(1)
