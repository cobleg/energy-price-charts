Under the Wholesale Electricity Market (WEM) Rules, reserve capacity payments are designed to compensate Market Participants for providing certified dispatchable capacity to meet the system's reliability standards. The payments are determined through a structured settlement process calculated for each Trading Day 1-3.  
With the introduction of the new Flexible Capacity product, the net Reserve Capacity settlement amount (RC\_SA) for a Market Participant is determined by calculating the sum of their **Peak Capacity** provider payments and **Flexible Capacity** provider payments, and then subtracting their respective purchaser obligations (charges) 4, 5\.

### 1\. Calculating the Capacity Provider Payment

For a given Trading Day, the payment a Market Participant receives for providing capacity is fundamentally based on the number of Capacity Credits they hold that are *not* traded bilaterally to other participants 2, 6\.  
The primary component of the payment is calculated as:**Capacity\_Payments \= (Capacity Credits \- Bilaterally Traded Credits) × Facility Daily Reserve Capacity Price** 2, 7\.  
The total **Capacity Provider Payment** then undergoes further adjustments. It includes the base capacity payments, plus any supplementary capacity payments or Participant Capacity Rebates, minus any **Capacity Cost Refunds** and **Intermittent Load Refunds** 7, 8\.

### 2\. Determining the Reserve Capacity Price

The WEM operates on an administered pricing mechanism rather than a pay-as-bid market 9\. The capacity price is determined using a prescribed price curve that depends on two main factors:

* **The Benchmark Reserve Capacity Price (BRCP):** This is determined annually by the Economic Regulation Authority (ERA) and reflects the expected annualised capital and fixed operations and maintenance costs of a theoretical "Benchmark Capacity Provider" (typically a new entrant open-cycle gas turbine or a large-scale battery) 10-12.  
* **The Level of Excess Capacity:** The final Reserve Capacity Price is dynamically adjusted based on the total supply of Capacity Credits relative to the Reserve Capacity Requirement. If there is a high surplus of capacity, the price drops; if capacity is tight, the price can increase up to a cap (historically 130% of the BRCP, or 150%/160% in newer formulas) 13-16.

Under recent market reforms, facilities are assigned **Peak Capacity Credits**, and eligible highly responsive facilities can concurrently be assigned **Flexible Capacity Credits** for the same MW of capacity 4\. Distinct prices are calculated for both products using their own specific benchmark costs (Peak BRCP and Flexible BRCP) and demand curves 14, 15\.

### 3\. Deductions for Failing to Meet Obligations (Capacity Cost Refunds)

While capacity payments are fixed per credit, providers must physically make that capacity available in the real-time and day-ahead markets 17\. If a facility fails to meet its Reserve Capacity Obligation Quantity (RCOQ), it faces financial penalties known as **Facility Reserve Capacity Deficit Refunds** (or Capacity Cost Refunds) which are subtracted directly from their capacity payments 8, 18, 19\.  
Refunds are triggered by shortfalls such as:

* The facility experiencing a **Forced Outage** or Refund Payable Planned Outage 20, 21\.  
* The participant failing to offer sufficient capacity into the Real-Time Market 21\.  
* For Electric Storage Resources (batteries), failing to maintain an adequate state of charge (ESR Charge Shortfall) during their designated obligation intervals 21, 22\.

To strongly penalise unavailability when the grid is under stress, a "dynamic refund factor" multiplier is applied. This means a facility may have to refund up to six times the daily capacity price for the interval they failed to generate, inversely proportional to how much spare capacity was left in the entire system at that time 23-25.

### 4\. Funding the Payments (Purchaser Charges)

To fund these capacity payments, the WEM Rules allocate the costs to Market Customers (retailers and large consumers). AEMO calculates a **Targeted Reserve Capacity Cost** and a **Shared Reserve Capacity Cost** for each Trading Day 26, 27\.  
These costs are charged to Market Participants based on their **Individual Reserve Capacity Requirement (IRCR)** 19, 28\. A participant's IRCR is determined by their historical metered consumption during the 12 highest peak demand intervals of the previous hot season, ensuring that the entities driving peak system demand pay a proportional share of the capacity procured to service that peak 29\.  
