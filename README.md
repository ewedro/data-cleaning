# data-cleaning
Each record in the HADS dataset represents one sampled housing unit

OWNRENT variable
-Rental: Occupied units rented for cash and without payment of cash rent. Vacant for rent,
vacant for rent or sale, and rented but not occupied.
-Owner: Owner occupied, vacant for sale, and sold but not occupied.

The monthly housing cost variables are COST06, COST08, COST12, and COSTMED

For renters, housing cost is contract rent plus utility costs.

Definition of Owner Costs
Actual housing cost expenditures for owner-occupied units vary whether or not the household has a mortgage and, among mortgaged units, because of the historical contingency of the market interest rate when each household obtained or refinanced its mortgage. In order to measure affordability free of this contingency, we assume that owners hold fully amortizing 30-year fixed rate mortgages with 10 percent down payments.8
The four basic cost measures are estimates of mortgage payments at 6, 8, and 12 per cent interest rates, plus the median interest rate in the AHS dataset for the survey year.9
The amount financed is assumed to be the value of the unit, minus 10 per cent for the down payment. To each basic cost are added utility cost, other cost (see
below), and an allowance for property insurance and property taxes. The combined amount of taxes and insurance is set at 1.5 percent of value per year

A separate utility cost variable (UTILITY) is included in the dataset, the sum of all applicable utility
costs.
For each utility (gas, oil, electricity, other fuel, trash collection, and water), the allocation matrix has
four dimensions:
• Monthly rent or mortgage payment (16 categories, $100 intervals). We estimate the mortgage
payment the same way as in the housing cost section above, assuming an 8 per cent interest rate.
• Structure type (2 categories). Single-unit or multi-unit.11
• Region (4 categories). The four Census regions.
• Tenure (2 categories). Owner or renter.

A separate variable (OTHERCOST) is the sum of these items.
• Home owners’ or renters’ insurance. For vacant units, this is allocated by the same hot-deck
procedure as utility cost.
• Land rent, where distinct from unit rent.
• Condominium fees, where applicable.
• Other mobile home fees, where applicable.

Housing cost burden is simply a household’s monthly housing cost divided by its monthly income. 
Households with zero or negative income are given the special code of BURDEN = -1. Vacant units, not being households, have missing values for BURDEN.

Total salary income (TotSal) is useful for identifying the “working poor” and measuring the labor force
attachment of a household. This variable is simply the sum of wage and salary income (Sal) over all members
of the household.

What we are calling AMI is actually based on four related income measures:
1. Median Income (LMed), which is not adjusted for the number of persons in the household.
2. Low Income (L80), which is adjusted for the number of persons in the household.
3. Very Low Income (L50), which is adjusted for the number of persons in the household.
4. Extremely Low Income (L30), which is adjusted for the number of persons in the household. L30
is available in the AHS PUF only for 2003 and later national surveys. 