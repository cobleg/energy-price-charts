"""
Aggregates wem_balancing_market.json to monthly summaries.
Outputs a JS snippet ready to embed in the dashboard.
"""

import json, statistics, os

SRC  = r"F:\Data\Energy prices\wem_balancing_market.json"
OUT  = r"F:\Data\Energy prices\_balancing_monthly.json"

with open(SRC, encoding="utf-8") as f:
    data = json.load(f)["data"]

# Group by YYYY-MM
months = {}
for r in data:
    key = r["trading_date"][:7]          # "YYYY-MM"
    if key not in months:
        months[key] = []
    months[key].append(r)

results = []
for key in sorted(months.keys()):
    rows = months[key]
    prices = [r["final_price_mwh"] for r in rows if r["final_price_mwh"] is not None]
    gen    = [r["total_gen_mw"]    for r in rows if r["total_gen_mw"]    is not None]

    # MWh = MW * 0.5h per 30-min interval
    gen_sum_mwh = sum(gen) * 0.5

    results.append({
        "month":        key,
        "gen_count":    len(rows),
        "gen_sum":      round(gen_sum_mwh, 2),          # MWh
        "gen_mean":     round(statistics.mean(gen),  3) if gen    else None,
        "price_mean":   round(statistics.mean(prices), 4) if prices else None,
        "price_median": round(statistics.median(prices), 4) if prices else None,
        "price_min":    round(min(prices), 4) if prices else None,
        "price_max":    round(max(prices), 4) if prices else None,
        "price_std":    round(statistics.stdev(prices), 4) if len(prices) > 1 else None,
        "market":       "balancing",
    })

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print(f"Written {len(results)} monthly rows to {OUT}")
print(f"Coverage: {results[0]['month']} → {results[-1]['month']}")
print("\nInterval counts per month (check for anomalies):")
for r in results:
    flag = " *** LOW" if r["gen_count"] < 1300 else ""
    print(f"  {r['month']}: {r['gen_count']:5d} intervals  gen_sum={r['gen_sum']:>12,.0f} MWh  "
          f"price_mean={r['price_mean']:>7.2f}  price_min={r['price_min']:>8.2f}  "
          f"price_max={r['price_max']:>7.2f}{flag}")
