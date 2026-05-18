# File Catalogue — Energy Prices Working Folder

**Folder:** `F:\Data\Energy prices`
**Last updated:** 17 May 2026 (fifth revision)
**Total files:** 30 (11 Excel workbooks, 1 PDF, 4 CSV tables, 7 Markdown notes, 7 derived HTML analyses, this catalogue makes 31)

This catalogue groups the contents of the working folder by source and topic, then lists the full inventory for each file (sheet/tab names, dimensions, key fields, time coverage, and a content summary). Source data files are listed in groups 1 through 7; derived HTML outputs produced during the May 2026 analysis sessions are listed in group 8.

---

## Group 1 — ABS Consumer Price Index (CPI) data

Source: Australian Bureau of Statistics, catalogue **6401.0 Consumer Price Index, Australia**.

Three workbooks covering different CPI tables and frequencies. All follow the standard ABS Time Series Workbook template: an `Index` sheet listing every series with Series ID and metadata, one or more `Data*` sheets containing the time series in wide format (columns = series, rows = time periods), and an `Enquiries` sheet with ABS contact details.

### 1.1 `ABS 6401010 - 20260514.xlsx`

| Field | Value |
| :---- | :---- |
| Size | 720,962 bytes |
| Last modified | 14 May 2026 |
| ABS Table | Table 10 — CPI: Group, Sub-group and Expenditure Class, Index Numbers by Capital City |
| Frequency | Monthly |
| Series type | Original |
| Coverage | Capital city level; recent monthly CPI series |
| Latest observation | January 2026 |
| Sheets (9) | `Index` (1,069 rows × 13 cols), `Energy Summary` (152 × 39), `Telecom Prices` (54 × 22), `Data1`–`Data4` (each 111 × 251), `Data5` (111 × 57), `Enquiries` (11 × 26) |
| Key fields per series | Data Item Description, Series Type, Series ID, Unit, Data Type, Frequency, Series Start, Series End, No. Obs |
| Notes | Includes a curated `Energy Summary` sheet and a `Telecom Prices` sheet alongside the raw data sheets. Series start dates vary by expenditure class (e.g., 2017‑09 for Bread, 2024‑04 for All groups CPI under the current monthly basis). |

### 1.2 `ABS 6401018 - 20260514.xlsx`

| Field | Value |
| :---- | :---- |
| Size | 489,566 bytes |
| Last modified | 14 May 2026 |
| ABS Table | Table 18 — CPI: Quarterly Group, Sub-group and Expenditure Class, Weighted Average of Eight Capital Cities |
| Frequency | Quarterly |
| Series type | Original |
| Coverage | National (weighted average of eight capital cities) |
| Latest observation | December 2025 quarter |
| Sheets (5) | `Index` (409 × 13), `Energy Prices` (189 × 25), `Data1` (320 × 251), `Data2` (320 × 147), `Enquiries` (11 × 26) |
| Key fields per series | Data Item Description, Series Type, Series ID, Unit, Frequency, Series Start, Series End, No. Obs |
| Notes | The `All groups CPI ; Australia` series runs from 1948‑09 (310 quarterly observations). Contains a dedicated `Energy Prices` sheet that aggregates energy-related expenditure classes. |

### 1.3 `ABS 640107 - previous series - 20260514.xlsx`

| Field | Value |
| :---- | :---- |
| Size | 1,663,302 bytes (largest source file in the folder) |
| Last modified | 14 May 2026 |
| ABS Table | Table 9 (legacy/previous series) — CPI: Group, Sub-group and Expenditure Class, Index Numbers by Capital City |
| Frequency | Quarterly |
| Series type | Original |
| Coverage | Capital city level — historical series ending in the June 2019 quarter |
| Latest observation | June 2019 quarter (this is the discontinued legacy series) |
| Sheets (9) | `Index` (1,381 × 13), `Energy Summary` (166 × 62), `Data1`–`Data5` (each 294 × 251), `Data6` (294 × 119), `Inquiries` (12 × 26) |
| Notes | The "previous series" label indicates this is the prior CPI compilation methodology, retained for long-run historical analysis. Bread by Sydney runs from 1980‑09 to 2019‑06 (156 observations). |

---

## Group 2 — ABS Producer Price Index (PPI) data

### 2.1 `ABS 6427013 - 20260514.xlsx`

| Field | Value |
| :---- | :---- |
| Size | 306,689 bytes |
| Last modified | 14 May 2026 |
| ABS Catalogue | 6427.0 Producer Price Indexes, Australia |
| ABS Table | Table 13 — Inputs from selected Subdivisions and Groups to the Manufacturing Division, index numbers and percentage changes |
| Frequency | Quarterly |
| Series type | Original |
| Coverage | Manufacturing inputs — index numbers and quarter-on-quarter % changes |
| Latest observation | March 2026 quarter |
| Sheets (5) | `Index` (75 × 13), `Data1` (241 × 63), `Enquiries` (11 × 26), `Summary Stats` (44 × 11), `Charts` (282 × 20) |
| Key series | Manufacturing division (A2309054F, from 1968‑09), Imported materials (A2313785L), Domestic materials (A2313788V), Manufacturing div. less petroleum (A2313704X, from 1987‑09) |
| Notes | Useful for tracking input-cost inflation feeding into manufacturing — particularly the imported vs. domestic materials split and petroleum-stripped index. |

---

## Group 3 — ABS Private New Capital Expenditure data

Source: Australian Bureau of Statistics, catalogue **5625.0 Private New Capital Expenditure and Expected Expenditure, Australia**.

Both workbooks share the same underlying survey but report different measures. They include an `EGWW` (Electricity, Gas, Water and Waste services) breakout, which is the energy-relevant industry slice. The 5625.0 survey covers **private** businesses only and excludes public-sector entities (relevant when comparing to 5204.0 GFCF below).

### 3.1 `ABS 01_current_prices_original_capex - 20260514.xlsx`

| Field | Value |
| :---- | :---- |
| Size | 193,955 bytes |
| Last modified | 14 May 2026 |
| ABS Table | Table 1 — Actual Expenditure, by Type of Asset and Industry, Original, Current Prices ($m) |
| Frequency | Quarterly |
| Series type | Original |
| Coverage | Total (State), Buildings and Structures, current prices, by industry including Mining, Manufacturing, Non-Mining |
| Latest observation | December 2025 quarter |
| Sheets (4) | `Index` (70 × 13), `Data1` (165 × 58), `Energy Utilities` (160 × 11), `Enquiries` (12 × 26) |
| Notes | Contains a dedicated `Energy Utilities` sheet — the energy-specific cut of the broader capex survey. Series run from 1987‑06. ABS asset-type definitions: *Buildings and Structures* includes power and telephone lines, pipelines, water/sewerage installations and structures-integral HVAC; *Equipment, Plant and Machinery* covers loose plant, vehicles, electrical apparatus, office equipment and special tooling. |

### 3.2 `ABS 08_volume_measures_trend_capex - 20260514.xlsx`

| Field | Value |
| :---- | :---- |
| Size | 164,936 bytes |
| Last modified | 14 May 2026 |
| ABS Table | Table 8 — Actual Expenditure, by Type of Asset and Industry, Trend, Chain Volume Measures ($m) |
| Frequency | Quarterly |
| Series type | Trend |
| Coverage | Same industries as Table 1 but reported in chain volume measures (real terms) and trend-smoothed |
| Latest observation | December 2025 quarter |
| Sheets (5) | `Index` (70 × 13), `Data1` (164 × 58), `Enquiries` (12 × 26), `EGWW Capex` (159 × 7), `EGWW Equipment` (159 × 7) |
| Notes | The EGWW sheets isolate Electricity, Gas, Water and Waste services capex into Total and Equipment-only views — useful for tracking real energy-sector investment over time. Series run from 1987‑09. |

---

## Group 4 — ABS National Accounts Gross Fixed Capital Formation (GFCF)

Source: Australian Bureau of Statistics, catalogue **5204.0 Australian System of National Accounts**.

Two workbooks added 14 May 2026 that complement the 5625.0 capex data above. The key difference: 5204.0 reports **National Accounts GFCF** which (unlike 5625.0) includes **public corporations** as well as private businesses, and uses the full SNA08 asset classification — splitting capital formation into Non-dwelling construction, Machinery and equipment, IP products (R&D and computer software), and Cultivated biological resources. These are annual data, not quarterly.

### 4.1 `ABS 5204054_Public_Corp_GFCF - 20260514.xlsx`

| Field | Value |
| :---- | :---- |
| Size | 81,650 bytes |
| Last modified | 14 May 2026 |
| ABS Table | Table 54 — Public Corporations Gross Fixed Capital Formation, by Level of Government and Industry, Current prices |
| Frequency | Annual (financial year ending 30 June) |
| Series type | Original (Data Type: DERIVED) |
| Coverage | Public corporations only, split by level of government (Commonwealth / State and Local) and ANZSIC industry — Electricity, Gas, Water and Waste Services is one of the included industries |
| Time span | 1960 FY to 2025 FY (66 annual observations) |
| Sheets (4) | `Index` (73 × 13), `Chart1` (chart sheet), `Data1` (76 × 61), `Enquiries` (12 × 26) |
| Key series | Public corporations – Commonwealth – Electricity, gas, water and waste services (A3347613V); equivalent State/Local series sit further down the index |
| Notes | Captures the public-sector investment leg that 5625.0 excludes. Together with 5625.0 these workbooks span the full ownership spectrum of EGWW investment — essential for analysing the disaggregation period (1995 NCP) and the modern era of state-owned WA utilities (Synergy, Western Power, Horizon Power). |

### 4.2 `ABS 5204064_GFCF_By_Industry_Asset - 20260514.xlsx`

| Field | Value |
| :---- | :---- |
| Size | 173,356 bytes |
| Last modified | 14 May 2026 |
| ABS Table | Table 64 — Gross Fixed Capital Formation, by Industry by Type of Asset |
| Frequency | Annual (financial year ending 30 June) |
| Series type | Original (Data Type: DERIVED), Chain Volume Measures |
| Coverage | All-sector GFCF (public + private) by ANZSIC industry × SNA08 asset type |
| Time span | 1960 FY to 2025 FY (66 annual observations) |
| Sheets (4) | `Index` (239 × 13), `Chart1` (chart sheet), `Data1` (76 × 227), `Enquiries` (12 × 26) |
| Asset categories per industry | Non-dwelling construction · Machinery and equipment · Intellectual property products – Research and development · Intellectual property products – Computer software · Cultivated biological resources (for AFF only) · Gross fixed capital formation total |
| Notes | The most detailed asset × industry view — particularly useful for separating EGWW network capex (Non-dwelling construction) from generation plant (Machinery and equipment) and from software/control-system capex (IP products – Computer software). The IP categories are where modern grid-management, SCADA and trading systems sit. |

---

## Group 5 — Western Australian utility-level capital works data

Project-level capex data for WA's state-owned electricity and water utilities. Both files share the same schema (Financial Year Ending, Utility Name, Project Name, Project Expenditure, Notes) and cover the same FY2021–FY2027 window with actuals through FY2024 and forward forecasts thereafter. Together they cover all six major WA state-owned utilities operating under the EGWW (Electricity, Gas, Water and Waste Services) ANZSIC division.

### 5.1 `Western Australian Utility Capital Works Programs 2021-2027 - Table 1.csv` (electricity utilities)

| Field | Value |
| :---- | :---- |
| Size | 16,068 bytes |
| Last modified | 15 May 2026 |
| Format | CSV |
| Rows | 140 project-year entries (plus header) |
| Columns | Financial Year Ending, Utility Name, Project Name, Project Expenditure, Notes |
| Utilities (3) | Synergy (45 entries), Western Power (44), Horizon Power (51) |
| Years covered (7) | 2021 to 2027 financial years — actuals through 2024 and forward forecasts thereafter |
| Notes | Project-level granularity for WA's three state-owned electricity utilities. Covers Synergy's Total Asset Investment Program, Western Power's network capex and regulatory determinations, Horizon Power's remote-community programs, plus thematic line items (WEM reforms, ICT, VPPs, social-housing rooftop solar, metering, CER integration). Bridges the gap between aggregate ABS data and individual investment decisions in the SWIS — the closest available source to "what did the WA utilities actually spend money on, year by year." Some forward years carry `N/A` where individual project budgets sit inside larger multi-year aggregates. |

### 5.2 `Western Australian Water Utility Asset Investment Forecast 2021–2027 - Table 1.csv` (water utilities)

| Field | Value |
| :---- | :---- |
| Size | 6,578 bytes |
| Last modified | 15 May 2026 (new) |
| Format | CSV |
| Rows | 55 project-year entries (plus header) |
| Columns | Financial Year Ending, Utility Name, Project Name, Project Expenditure, Notes |
| Utilities (3) | Water Corporation (statewide, the bulk of entries), Bunbury Water Corporation, Busselton Water Corporation |
| Years covered (7) | 2021 to 2027 financial years |
| Project themes | Metropolitan Water Network and Supply, Wastewater Projects, Essential and Municipal Services Upgrade (Aboriginal communities), Groundwater Replenishment Scheme, METRONET pipe relocations, regional WWTP upgrades, COVID-19 response infrastructure, Bunbury Water Resource Recovery Scheme, Total Asset Investment Program headline figures |
| Notes | Sister file to 5.1, capturing the water-utility leg of the EGWW sector. Water Corporation alone runs a ~$700m–$2.7bn annual Asset Investment Program covering metropolitan supply, regional water and wastewater, and Indigenous community services. Useful when interpreting ABS 5625.0/5204.0 EGWW capex aggregates because it gives the water-side bottom-up view that the aggregate cannot disaggregate. |

---

## Group 6 — Global energy price data

### 6.1 `natural-gas-prices-world-bank-pink-sheets.xlsx`

| Field | Value |
| :---- | :---- |
| Size | 54,598 bytes |
| Last modified | 14 May 2026 |
| Source | World Bank Group — *Natural Gas Prices (World Bank Pink Sheets)* via FetchSeries (accessed 14 May 2026) |
| Frequency | Monthly |
| Coverage | Three regional benchmarks: United States, Europe, Japan (Liquefied natural gas) |
| Time span | 1960‑01 to present (~795 monthly observations) |
| Sheets (1) | `Natural gas prices` (801 × 6) |
| Columns | Date string, Date (datetime), US Natural gas (USD/MMBtu), Europe Natural gas (USD/MMBtu), Japan LNG (USD/MMBtu) |
| Notes | Long-run global gas benchmark series — the standard reference for international gas price comparisons. |

---

## Group 7 — Australian energy policy and history

Curated notes and reference tables that contextualise the data files above. Useful as source material for narrative sections of reports on Australian energy pricing.

### 7.1 `Australian Energy Subsidies and Consumer Relief Mechanisms.md`

| Field | Value |
| :---- | :---- |
| Size | 2,804 bytes |
| Last modified | 14 May 2026 |
| Format | Markdown table |
| Rows | 6 subsidy/intervention entries |
| Columns | Government Level, Name of Subsidy/Intervention, Target Consumers, Description |
| Coverage | Commonwealth Energy Bill Relief Fund; WA below-cost regulated retail tariffs, Tariff Equalisation Fund (Uniform Tariff Policy), feed-in tariffs (FiTs/DEBS), Domestic Gas Reservation Policy, state-based concession schemes |

### 7.2 `Evolution of the Western Australian Wholesale Electricity Market.md`

| Field | Value |
| :---- | :---- |
| Size | 3,703 bytes |
| Last modified | 14 May 2026 |
| Format | Markdown table |
| Rows | 13 policy / reform entries |
| Columns | Government Policy / Reform, Date Introduced, Impact on the WEM and WA Energy Sector |
| Coverage | National Competition Policy (1995) through to the "New WEM" SCED reforms (October 2023). Includes the SECWA breakup, Electricity Industry Act 2004, 2006 SWIS WEM launch, WA Domestic Gas Reservation Policy, Verve generation cap, Energy Transformation Strategy, Whole of System Plan, DER Roadmap, and the Just Transition Plan. |

### 7.3 `Chronicle of Australian Energy Policy Interventions (1975–2024) - Table 1.csv`

| Field | Value |
| :---- | :---- |
| Size | 3,708 bytes |
| Last modified | 14 May 2026 |
| Format | CSV |
| Rows | 34 policy interventions |
| Columns | Policy Intervention, Date of Introduction, Source Notes, Termination Date/Year, Termination Comment, Termination Source Note |
| Coverage | 1975 Import Parity Pricing for new oil → 2024 Energy Bill Relief Fund. Includes Hilmer Reforms, NEM establishment, AEMC/AER, WEM launch, all state feed-in tariffs, carbon tax 2012–14, ADGSM, Heads of Agreement with East Coast LNG exporters, DMO, RRO, PEMM, fuel excise cut, NSW coal price cap, temporary gas price cap, Mandatory Gas Market Code, and the Capacity Investment Scheme. |

### 7.4 `Climate and Geopolitical Shocks to Australian Energy Infrastructure - Table 1.csv`

| Field | Value |
| :---- | :---- |
| Size | 2,733 bytes |
| Last modified | 14 May 2026 |
| Format | CSV |
| Rows | 9 external shock entries |
| Columns | External Shock, Date / Period, Description of Event, Part of Energy System Directly Impacted |
| Coverage | 1973/79 oil shocks, Millennium Drought, 2008 GFC (network cost recovery channel), Cyclone Yasi 2011, SA storms 2016, COVID‑19 2020–21, 2022 floods affecting coal supply, 2022 Russian invasion of Ukraine (NEM suspension), February 2024 Victorian storms (transmission tower collapse). |

### 7.5 `Legacy Domestic Energy Contract Terms 1985–2005.md`

| Field | Value |
| :---- | :---- |
| Size | 2,667 bytes |
| Last modified | 17 May 2026 |
| Format | Markdown — structured reference note |
| Coverage | North West Shelf (NWS) Joint Venture domestic gas take-or-pay contracts with the State Energy Commission of Western Australia (SECWA), signed September 1980, operational 1985–2005 |
| Key figures | Contracted volume: 370 MMCFD (million cubic feet per day) total; SECWA obligated to draw 351 MMCFD (95%). Alcoa was SECWA's largest sub-customer at ~150 MMCFD (over half of gas piped to the South West). Upstream price: ~AUD $2–3/GJ, kept largely fixed under confidential coal- and oil-competitive pricing formulas; price never publicly disclosed. |
| Unit note | MMCFD is a volumetric flow rate. To convert to an energy rate: 1 MMCFD ≈ 1,113 GJ/day (using 1 standard cubic foot ≈ 1,055 BTU ≈ 1.113 MJ; 1 MMBtu = 1.0551 GJ). The 370 MMCFD contracted volume therefore represents approximately 150 PJ/year of energy delivery. The price of AUD $2–3/GJ converts to approximately AUD $2.11–3.16/MMBtu (× 1.0551); in USD at the prevailing AUD/USD rate of ~0.70–0.85, this equates to roughly USD $1.50–2.70/MMBtu — broadly comparable to US Henry Hub prices of the same era. |
| Sources | [1] Gardner, Robert Scott (1989), Murdoch University; [2] EnergyQuest for the Australian Energy Regulator (2009), *Australia's Natural Gas Markets: Connecting with the World* |
| Notes | Key pre-policy baseline for interpreting WA gas price history. The end of these fixed-price take-or-pay contracts (~2005) removed the regulatory floor that had kept WA upstream gas prices anchored at $2–3/GJ, creating the supply-security pressure that motivated the 2006 Domestic Gas Reservation Policy. |

---

## Group 8 — Derived analyses and visualisations

HTML outputs produced from the source data files during the May 2026 analysis sessions. All are self-contained single-file artefacts that open directly in a browser. They consume the source files in groups 1–7 above; if any source file is updated, the relevant HTML should be rebuilt.

### 8.1 `Energy_Prices_Chart.html`

| Field | Value |
| :---- | :---- |
| Size | 34,906 bytes |
| Created | 14 May 2026 |
| Source data | ABS 6401010 (current monthly), ABS 640107 (legacy quarterly) |
| Description | Interactive time-series chart of electricity and gas CPI by capital city. Toggles for time period (legacy 1989–2019 quarterly vs current 2021–2026 monthly), fuel (electricity / gas / both), and per-city visibility. |

### 8.2 `Energy_Prices_Chart_Annotated.html`

| Field | Value |
| :---- | :---- |
| Size | 42,022 bytes |
| Created | 14 May 2026 |
| Source data | ABS 6401010 + 640107 + `Australian Energy Subsidies and Consumer Relief Mechanisms.md` |
| Description | Same as 8.1 with overlaid subsidy-intervention callouts (WA Gas Reservation 2006, WA Premium FiT 2010–11, Commonwealth Energy Bill Relief Fund 2023–25). Includes structural-subsidy cards for items without a fixed start date. |

### 8.3 `Energy_Prices_Chart_Shocks.html`

| Field | Value |
| :---- | :---- |
| Size | 42,993 bytes |
| Created | 14 May 2026 |
| Source data | ABS 6401010 + 640107 + `Climate and Geopolitical Shocks…csv` |
| Description | Same as 8.1 with overlaid external-shock callouts (Millennium Drought, GFC, Cyclone Yasi, SA storms, 2022 floods, Russian invasion of Ukraine, Victorian transmission-tower collapse). Out-of-window shocks shown as context cards. |

### 8.4 `Energy_Prices_Chart_Unified.html`

| Field | Value |
| :---- | :---- |
| Size | 51,198 bytes |
| Created | 14 May 2026 |
| Source data | Combines all sources from 8.2 and 8.3 |
| Description | The combined view — subsidy interventions (S# badges) and external shocks (X# badges) on the same chart with independent on/off toggles. Square badges for subsidies, pill badges for shocks. |

### 8.5 `EGWW_Capex_vs_Electricity_Analysis.html`

| Field | Value |
| :---- | :---- |
| Size | 35,148 bytes |
| Created | 14 May 2026 |
| Source data | ABS 08_volume_measures_trend_capex (EGWW Capex + EGWW Equipment sheets) + ABS 6401018 Energy Prices sheet |
| Description | Quantitative analysis of the relationship between EGWW sector capex (chain volume trend) and the national electricity CPI 1987–2025. Includes dual-axis time series, scatter plots in levels and YoY% form for both capex measures, full summary-statistics table, lag-correlation matrix (–8 to +8 quarters), and a written interpretation section. Headline finding: levels correlation r = +0.90 is largely a co-trend artefact; YoY% correlation is essentially zero. |

### 8.6 `Energy_Prices_Chart_NEM_WEM_CPI.html`

| Field | Value |
| :---- | :---- |
| Size | ~38,600 bytes |
| Created | 15 May 2026 |
| Source data | ABS 6401010 + 640107 + ABS 6401018 (All Groups CPI national series) |
| Description | Electricity and gas price chart with NEM and WEM market-group buttons that pre-select the right cities in one click (NEM = Brisbane, Sydney, Canberra, Melbourne, Adelaide, Hobart; WEM = Perth), plus an overlay line for the national All Groups CPI as an inflation benchmark. Per-city chips remain available for fine adjustments, and the CPI line can be toggled off. CPI is broadcast from quarterly to monthly in the recent view (stepped within quarter). |

### 8.7 `WA_Utility_vs_ABS_EGWW.html`

| Field | Value |
| :---- | :---- |
| Size | 59,689 bytes |
| Created | 16 May 2026 |
| Source data | `Western Australian Utility Capital Works Programs 2021-2027 - Table 1.csv` + `Western Australian Water Utility Asset Investment Forecast 2021–2027 - Table 1.csv` + ABS 5204064_GFCF_By_Industry_Asset (EGWW GFCF) + ABS 01_current_prices_original_capex (5625.0) |
| Description | Interactive visualisation comparing bottom-up project-level capital investment by all six WA state-owned utilities (electricity: Synergy, Western Power, Horizon Power; water: Water Corporation, Bunbury Water, Busselton Water) against the top-down ABS national EGWW aggregates. Stacked bar charts allow drill-down into individual utility and project segments by clicking. Covers FY2021–FY2027 with actuals through FY2024 and forward forecasts thereafter. A key methodological note is embedded: the WA utilities are all public corporations and therefore appear in ABS 5204.0 (public + private) but are excluded from ABS 5625.0 (private only) — reconciling these two series requires adding the WA utility bottom-up totals to the 5625.0 figures. |

---

## Group 9 — WEM Reserve Capacity pricing

Reference material on the Western Australian Wholesale Electricity Market (WEM) Reserve Capacity mechanism: how capacity prices are determined, settled, and enforced. All four files were added 17 May 2026.

### 9.1 `Reserve Capacity Prices Since Market Start.xlsx`

| Field | Value |
| :---- | :---- |
| Size | 55,674 bytes |
| Last modified | 17 May 2026 |
| Source | WEM market data — Reserve Capacity prices by Capacity Year since market commencement |
| Frequency | Annual (one row per Capacity Year) |
| Coverage | WEM Reserve Capacity mechanism from market start (~2006) to present |
| Notes | Contains the historical time series of Reserve Capacity Prices (Peak and/or Flexible) and the Benchmark Reserve Capacity Price (BRCP) used to derive them. Useful for tracking long-run capacity price trends against the narrative in the Group 9 reference notes below and against the electricity CPI series in Groups 1–2. |

### 9.2 `The WEM Reserve Capacity Settlement and Pricing Framework.md`

| Field | Value |
| :---- | :---- |
| Size | 4,608 bytes |
| Last modified | 17 May 2026 |
| Format | Markdown — structured reference note |
| Coverage | End-to-end WEM reserve capacity settlement: capacity provider payment formula; BRCP determination by the ERA; Peak vs Flexible Capacity Credits; dynamic refund factor (up to 6× daily price for shortfalls during high-stress intervals); purchaser charges allocated via Individual Reserve Capacity Requirement (IRCR) based on peak consumption history |
| Notes | The most comprehensive of the four reserve capacity notes. Covers all four stages of settlement: provider payment, price determination, refund deductions, and purchaser charges. |

### 9.3 `Fixed Reserve Capacity Pricing and Dynamic Refund Structures.md`

| Field | Value |
| :---- | :---- |
| Size | 2,111 bytes |
| Last modified | 17 May 2026 |
| Format | Markdown — reference note |
| Coverage | Explains the core pricing paradox: the Reserve Capacity Price is fixed for the entire Capacity Year (annual determination via the BRCP price curve), but Capacity Cost Refund penalties are dynamic — varying per Trading Interval in inverse proportion to the system spare-capacity margin. A facility unavailable when the grid is stressed faces far larger penalties than one unavailable during a surplus period. |
| Notes | Content is substantively identical to 9.4 and 9.5 below; the three files appear to be parallel drafts of the same explanatory note under different working titles. |

### 9.4 `Stability and Fluctuations in Reserve Capacity Pricing.md`

| Field | Value |
| :---- | :---- |
| Size | 2,115 bytes |
| Last modified | 17 May 2026 |
| Format | Markdown — reference note |
| Coverage | Same subject as 9.3: fixed annual Reserve Capacity Price vs dynamic Capacity Cost Refund penalties. |
| Notes | Content substantively identical to 9.3 and 9.5. |

### 9.5 `The Fixed Structure of Reserve Capacity Pricing.md`

| Field | Value |
| :---- | :---- |
| Size | 2,111 bytes |
| Last modified | 17 May 2026 |
| Format | Markdown — reference note |
| Coverage | Same subject as 9.3: fixed annual Reserve Capacity Price vs dynamic Capacity Cost Refund penalties. |
| Notes | Content substantively identical to 9.3 and 9.4. |

### 9.6 `certified-reserve-capacity-assigned-for-the-2027-28-capacity-year.pdf`

| Field | Value |
| :---- | :---- |
| Size | 215,648 bytes |
| Last modified | 17 May 2026 |
| Source | AEMO — *Summary of Certified Reserve Capacity Assigned by Facility for the 2025 Reserve Capacity Cycle* |
| Format | PDF, 4 pages |
| Capacity Year | 1 October 2027 to 1 October 2028 (the 2025 RC Cycle) |
| Totals | 6,375.141 MW Peak CRC assigned; 4,077.068 MW Flexible CRC assigned |
| Regulatory basis | ESM Rules clauses 4.9.9A (Flexible CRC) and 4.1.15A (Peak CRC) |
| Content | Two tables. **Table 1** lists every facility that has been assigned CRC and completed its Bilateral Trade Declaration and Reserve Capacity Security obligations — four columns: Market Participant Name, Facility Name, 2027-28 Peak CRC (MW), 2027-28 Flexible CRC (MW). Covers ~70 facilities across all technology types (gas peakers, CCGTs, wind farms, large BESS, solar PV, DSPs, hydro, biogas, landfill gas, WtE). **Table 2** shows the next steps in the 2025 RC Cycle (21 Oct, 22 Oct, 20 Nov, 27 Nov 2025), including NAQ allocation, Capacity Credit finalisation, RCS recalculation window, and publication of Reserve Capacity Prices. |
| Key participants | Synergy (largest by count, ~30 facilities); Alinta Sales (8 facilities); Collie Battery / Collie ESR4 / ESR5 (500 MW BESS, fully flexible); NewGen Neerabup GT1 (330.6 MW Peak, 330 MW Flexible); NewGen Kwinana CCG1 (327.8 MW Peak, 183 MW Flexible); Kemerton GT11/GT12 (151.919 MW each, fully flexible). |
| Relationship to 9.7 | CRC assignments here are the *indicative* pre-NAQ values; the finalised Capacity Credits (post-NAQ) for prior years are the time-series data in 9.7. The 2027-28 year is not yet in 9.7. |
| Notes | CRC is indicative only — AEMO must subsequently allocate Network Access Quantity (NAQ) against network constraints before Peak Capacity Credits and Flexible Capacity Credits are finalised on 21 October 2025. Facilities without Flexible CRC are either non-dispatchable (wind/solar, some DSPs) or gas plant without storage headroom to qualify. |

### 9.7 `WEM_aemo_capacity_credits_combined.xlsx`

| Field | Value |
| :---- | :---- |
| Size | 46,195 bytes |
| Last modified | 17 May 2026 |
| Source | Compiled from AEMO WEM market data — participant registry and capacity credit assignment history |
| Sheets (3) | `Market Participants`, `participants_2025-09-07T12-03-2`, `Capacity Credits by Year` |

**Sheet 1 — `Market Participants`** (64 rows × 7 cols)

Registered WEM market participants — every entity that has held or applied for a participant code. Columns: Organisation Name, Participant Code, ABN, ACN, Entity Type, Source (ABR/ASIC URL), secondary source URL. Entity types include Pty Ltd, Statutory Corporation, and Australian Proprietary Company Limited by Shares. Source links resolve to ABR and ASIC Connect Online for ABN and ACN verification.

**Sheet 2 — `participants_2025-09-07T12-03-2`** (41 rows × 6 cols)

Point-in-time snapshot dated 7 September 2025 of participants holding assigned Capacity Credits. Columns: Code, Participant, facilities (count), Total MW, Remaining MW, link (relative API path). Covers 41 participants ranging from Synergy (2,915 MW across 27 facilities) down to sub-1 MW participants. `Remaining MW` is populated only for a small subset (participants with headroom between their CRC and current credit assignment); most entries are NaN. Useful for a cross-section of the WEM generation mix at a single point in time.

**Sheet 3 — `Capacity Credits by Year`** (462 rows × 7 meaningful cols)

Facility-level Capacity Credit assignments over multiple RC Cycles. Columns: Participant, Participant Code, Facility, Facility Class, Capacity Credits MW, Reserve Capacity Cycle, Capacity Year. Four trailing columns are blank artefacts. RC Cycles covered: 2017–2023 (seven cycles); Capacity Years covered: 2019-20 through 2025-26. One data-quality issue: row 460 has a concatenated cell in the Capacity Year field (`"2024-25TIWEST_COG1"` — a merge artefact). Facility classes: Demand Side Programme · Non-Scheduled Facility · Non-Scheduled Generator · Scheduled Facility · Scheduled Generator · Semi-Scheduled Facility.

| Field | Value |
| :---- | :---- |
| RC Cycles | 2017, 2018, 2019, 2020, 2021, 2022, 2023 |
| Capacity Years | 2019-20 to 2025-26 |
| Facility classes | Demand Side Programme, Non-Scheduled Facility, Non-Scheduled Generator, Scheduled Facility, Scheduled Generator, Semi-Scheduled Facility |
| Notes | The most detailed longitudinal view of individual facility Capacity Credit holdings in the working folder. Useful for tracking entry/exit of participants, technology mix shifts (growth of BESS and Non-Scheduled / Semi-Scheduled renewables), and year-on-year credit changes per facility. Cross-reference Sheet 2 for the 2025 snapshot and 9.6 for the 2027-28 forward CRC assignments. The `Capacity Credits MW` column contains finalised credits post-NAQ (unlike the indicative CRC in 9.6). |

---

## Summary table — all files

| # | Filename | Group | Type | Size (bytes) |
| -: | :---- | :---- | :---- | -: |
| 1 | ABS 6401010 - 20260514.xlsx | 1 CPI | .xlsx | 720,962 |
| 2 | ABS 6401018 - 20260514.xlsx | 1 CPI | .xlsx | 489,566 |
| 3 | ABS 640107 - previous series - 20260514.xlsx | 1 CPI | .xlsx | 1,663,302 |
| 4 | ABS 6427013 - 20260514.xlsx | 2 PPI | .xlsx | 306,689 |
| 5 | ABS 01_current_prices_original_capex - 20260514.xlsx | 3 Private capex (5625.0) | .xlsx | 193,955 |
| 6 | ABS 08_volume_measures_trend_capex - 20260514.xlsx | 3 Private capex (5625.0) | .xlsx | 164,936 |
| 7 | ABS 5204054_Public_Corp_GFCF - 20260514.xlsx | 4 National Accts GFCF (5204.0) | .xlsx | 81,650 |
| 8 | ABS 5204064_GFCF_By_Industry_Asset - 20260514.xlsx | 4 National Accts GFCF (5204.0) | .xlsx | 173,356 |
| 9 | Western Australian Utility Capital Works Programs 2021-2027 - Table 1.csv | 5 WA utility capex (electricity) | .csv | 16,068 |
| 10 | Western Australian Water Utility Asset Investment Forecast 2021–2027 - Table 1.csv | 5 WA utility capex (water) | .csv | 6,578 |
| 11 | natural-gas-prices-world-bank-pink-sheets.xlsx | 6 Global prices | .xlsx | 54,598 |
| 12 | Australian Energy Subsidies and Consumer Relief Mechanisms.md | 7 Policy notes | .md | 2,804 |
| 13 | Evolution of the Western Australian Wholesale Electricity Market.md | 7 Policy notes | .md | 3,703 |
| 14 | Chronicle of Australian Energy Policy Interventions (1975–2024) - Table 1.csv | 7 Policy chronicle | .csv | 3,708 |
| 15 | Climate and Geopolitical Shocks to Australian Energy Infrastructure - Table 1.csv | 7 Shocks | .csv | 2,733 |
| 16 | Legacy Domestic Energy Contract Terms 1985–2005.md | 7 Policy notes | .md | 2,667 |
| 17 | Energy_Prices_Chart.html | 8 Derived | .html | 34,906 |
| 18 | Energy_Prices_Chart_Annotated.html | 8 Derived | .html | 42,022 |
| 19 | Energy_Prices_Chart_Shocks.html | 8 Derived | .html | 42,993 |
| 20 | Energy_Prices_Chart_Unified.html | 8 Derived | .html | 51,198 |
| 21 | EGWW_Capex_vs_Electricity_Analysis.html | 8 Derived | .html | 35,148 |
| 22 | Energy_Prices_Chart_NEM_WEM_CPI.html | 8 Derived | .html | 38,546 |
| 23 | WA_Utility_vs_ABS_EGWW.html | 8 Derived | .html | 59,689 |
| 24 | Reserve Capacity Prices Since Market Start.xlsx | 9 WEM Reserve Capacity | .xlsx | 55,674 |
| 25 | The WEM Reserve Capacity Settlement and Pricing Framework.md | 9 WEM Reserve Capacity | .md | 4,608 |
| 26 | Fixed Reserve Capacity Pricing and Dynamic Refund Structures.md | 9 WEM Reserve Capacity | .md | 2,111 |
| 27 | Stability and Fluctuations in Reserve Capacity Pricing.md | 9 WEM Reserve Capacity | .md | 2,115 |
| 28 | The Fixed Structure of Reserve Capacity Pricing.md | 9 WEM Reserve Capacity | .md | 2,111 |
| 29 | certified-reserve-capacity-assigned-for-the-2027-28-capacity-year.pdf | 9 WEM Reserve Capacity | .pdf | 215,648 |
| 30 | WEM_aemo_capacity_credits_combined.xlsx | 9 WEM Reserve Capacity | .xlsx | 46,195 |
