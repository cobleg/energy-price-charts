"""
Merges all WEM balancing-summary-YYYY.csv files into a single JSON.
Normalises date/datetime formats to ISO 8601.
Output: wem_balancing_market.json
"""

import csv
import json
import os

FOLDER = r"F:\Data\Energy prices"
OUTPUT = os.path.join(FOLDER, "wem_balancing_market.json")


def parse_date(s):
    """Normalise trading date to YYYY-MM-DD regardless of source format."""
    s = s.strip().strip('"')
    if len(s) >= 10 and s[4] == '-':        # already YYYY-MM-DD
        return s[:10]
    parts = s.split('/')                     # D/MM/YYYY
    return f"{int(parts[2]):04d}-{int(parts[1]):02d}-{int(parts[0]):02d}"


def parse_datetime(s):
    """Normalise datetime to ISO 8601 (YYYY-MM-DDTHH:MM:SS). Returns None if empty."""
    s = s.strip().strip('"')
    if not s:
        return None
    if len(s) >= 10 and s[4] == '-':        # YYYY-MM-DD HH:MM:SS
        return s.replace(' ', 'T')
    # D/MM/YYYY H:MM or D/MM/YYYY HH:MM
    parts = s.split(' ', 1)
    d = parts[0].split('/')
    t_parts = (parts[1] if len(parts) > 1 else '00:00').split(':')
    hh = int(t_parts[0])
    mm = int(t_parts[1]) if len(t_parts) > 1 else 0
    ss = int(t_parts[2]) if len(t_parts) > 2 else 0
    return f"{int(d[2]):04d}-{int(d[1]):02d}-{int(d[0]):02d}T{hh:02d}:{mm:02d}:{ss:02d}"


def to_float(s):
    s = s.strip()
    return float(s) if s else None


def to_int(s):
    s = s.strip()
    return int(s) if s else None


files = sorted(
    f for f in os.listdir(FOLDER)
    if f.startswith('balancing-summary-') and f.endswith('.csv')
)

print(f"Processing {len(files)} files...")

records = []
for fname in files:
    path = os.path.join(FOLDER, fname)
    with open(path, newline='', encoding='utf-8') as fh:
        reader = csv.reader(fh)
        next(reader)  # skip header
        count = 0
        for row in reader:
            if len(row) < 9:
                continue
            rec = {
                "trading_date":          parse_date(row[0]),
                "interval":              to_int(row[1]),
                "trading_interval":      parse_datetime(row[2]),
                "load_forecast_mw":      to_float(row[3]),
                "forecast_as_at":        parse_datetime(row[4]),
                "scheduled_gen_mw":      to_float(row[5]),
                "non_scheduled_gen_mw":  to_float(row[6]),
                "total_gen_mw":          to_float(row[7]),
                "final_price_mwh":       to_float(row[8]),
            }
            if len(row) > 9 and row[9].strip():
                rec["extracted_at"] = parse_datetime(row[9])
            records.append(rec)
            count += 1
    print(f"  {fname}: {count:,} intervals  ({records[0]['trading_date'] if records else '?'} … {records[-1]['trading_date']})")

output = {
    "metadata": {
        "title": "WEM Balancing Market — 30-Minute Interval Price and Generation Summary",
        "market": "Wholesale Electricity Market (WEM)",
        "region": "Western Australia — South West Interconnected System (SWIS)",
        "mechanism": "WEM Balancing Market (pre-October 2023 market structure)",
        "description": (
            "30-minute trading interval records of Balancing Market clearing prices "
            "and generation quantities for the full available history of the WEM Balancing Market, "
            "from 1 July 2012 through to 30 September 2023. "
            "From October 2023 the Balancing Market was replaced by the new WEM market structure "
            "(Real-Time Market and Reference Trading Price mechanism)."
        ),
        "coverage": {
            "start": records[0]["trading_date"],
            "end":   records[-1]["trading_date"],
            "total_intervals": len(records),
            "files_merged": files,
        },
        "timezone": "AWST (UTC+8) — no daylight saving. Trading day commences at 08:00 AWST (interval 1).",
        "units": {
            "load_forecast_mw":     "MW",
            "scheduled_gen_mw":     "MW",
            "non_scheduled_gen_mw": "MW",
            "total_gen_mw":         "MW",
            "final_price_mwh":      "AUD/MWh",
        },
        "source": {
            "provider":    "Australian Energy Market Operator (AEMO)",
            "url":         "https://www.aemo.com.au/energy-systems/electricity/wholesale-electricity-market-wem/data-wem/market-data-wa",
            "description": "AEMO WEM Balancing Market summary files, published annually",
            "accessed":    "2025-10-10",
        },
        "notes": [
            "The earliest available file (balancing-summary-2012.csv) commences 1 July 2012; earlier data is not included in this extract.",
            "The WEM Balancing Market operated from market start in January 2006 until the WEM reform launch in October 2023.",
            "Trading intervals are numbered 1–48 per trading day, with interval 1 commencing at 08:00 AWST.",
            "Scheduled Generation: dispatchable plant dispatched by AEMO via the Balancing Merit Order.",
            "Non-Scheduled Generation: non-dispatchable sources (wind, solar, small embedded) not subject to central dispatch.",
            "Final Price: the Balancing Market clearing price; set by the marginal scheduled generator or floor/cap in that interval.",
            "Source date formats normalised to ISO 8601 (YYYY-MM-DD / YYYY-MM-DDTHH:MM:SS) across all years.",
        ],
    },
    "columns": {
        "trading_date":          "Calendar date of the trading day (ISO 8601: YYYY-MM-DD, AWST)",
        "interval":              "Trading interval number within the day (1–48; interval 1 = 08:00–08:30 AWST)",
        "trading_interval":      "Start datetime of the 30-minute trading interval (ISO 8601, AWST)",
        "load_forecast_mw":      "AEMO's forecast of total system load at the time of the pre-dispatch run (MW)",
        "forecast_as_at":        "Datetime at which the load forecast was generated (ISO 8601, AWST)",
        "scheduled_gen_mw":      "Total dispatched scheduled (dispatchable) generation for the interval (MW)",
        "non_scheduled_gen_mw":  "Total non-scheduled (non-dispatchable) generation including wind and solar (MW)",
        "total_gen_mw":          "Total system generation: scheduled + non-scheduled (MW)",
        "final_price_mwh":       "Final Balancing Market clearing price for the interval (AUD/MWh)",
        "extracted_at":          "Timestamp at which the record was extracted from the AEMO system (ISO 8601; present on most but not all records)",
    },
    "data": records,
}

with open(OUTPUT, 'w', encoding='utf-8') as fh:
    json.dump(output, fh, separators=(',', ':'))

size_mb = os.path.getsize(OUTPUT) / 1e6
print(f"\nDone. Written {len(records):,} intervals to:")
print(f"  {OUTPUT}")
print(f"  Size: {size_mb:.1f} MB")
print(f"  Coverage: {records[0]['trading_date']} to {records[-1]['trading_date']}")
