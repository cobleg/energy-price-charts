# Australian Energy Prices — Interactive Charts

A collection of self-contained interactive HTML charts exploring Australian electricity and gas prices, WEM wholesale market data, international gas benchmarks, and utility capital expenditure analysis.

## Charts

| Chart | Description |
|-------|-------------|
| [Electricity & Gas CPI by Capital City](Energy_Prices_Chart.html) | ABS CPI series across all 8 capital cities, 1989–2026 |
| [Annotated — Government Subsidies](Energy_Prices_Chart_Annotated.html) | Policy and bill-relief interventions overlaid |
| [Annotated — Climate & Geopolitical Shocks](Energy_Prices_Chart_Shocks.html) | External shock events overlaid |
| [Unified Annotated View](Energy_Prices_Chart_Unified.html) | Both annotation layers combined |
| [NEM vs WEM with CPI Overlay](Energy_Prices_Chart_NEM_WEM_CPI.html) | NEM/WEM comparison against all-groups CPI |
| [WEM Composite Price Dashboard](wem_composite_price_dashboard.html) | Balancing market + reserve capacity, 2012–2026 |
| [WEM Sent-Out Energy & Trading Prices](sent_out_trading_prices_dashboard.html) | Monthly WEM generation and trading prices, 2023–2026 |
| [Gas Prices vs International Benchmarks](Gas_Price_International_Comparison.html) | Henry Hub, NBP/TTF, Japan LNG CIF vs Australian retail |
| [EGWW Capex vs Electricity Prices](EGWW_Capex_vs_Electricity_Analysis.html) | Correlation analysis of sector capex and consumer prices |
| [WA Utility Capex vs ABS EGWW](WA_Utility_vs_ABS_EGWW.html) | Bottom-up WA utility projects vs ABS national aggregates |

## Data Sources

- **ABS Catalogue 6401.0** — Consumer Price Index, Australia
- **AEMO / WEM Market Operator** — Wholesale electricity market data
- **IEA** — International gas price benchmarks

## Hosting on GitHub Pages

1. Create a new repository on GitHub (public)
2. Push this folder's contents to the `main` branch
3. Go to **Settings → Pages → Source** and set branch to `main`, folder to `/ (root)`
4. Your site will be live at [https://cobleg.github.io/energy-price-charts/](https://cobleg.github.io/energy-price-charts/)

All charts are self-contained — Chart.js loads from CDN, no build step required.
