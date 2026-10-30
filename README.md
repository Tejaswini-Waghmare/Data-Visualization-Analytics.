# Data Visualization & Analytics — Learning Repository

Eight guided modules on charts, statistical visuals, interactive exploration, dashboards, and business storytelling. Uses **600 synthetic retail orders** (not real company data). Every module includes notes, a notebook, exercises, and solutions.

## Quick start
```bash
python -m pip install -r requirements.txt
jupyter notebook
```
Open any module's `Examples.ipynb` from the repository root. Notebooks find the shared `data/retail_orders_synthetic.csv` using a relative-path fallback. In Google Colab, upload the CSV into the session's Files panel.

## Data definitions
`gross_sales = units * unit_price`; `net_sales = gross_sales * (1 - discount_rate)`; `profit = net_sales - cost`. Revenue/profit analyses include **Completed** orders only; returns and cancellations are excluded, not counted as negative sales. `customer_rating` is simulated and should not be treated as a validated satisfaction metric.

## Modules
- [01_Visualization_Fundamentals](./01_Visualization_Fundamentals): Choosing chart types, visual encoding, labeling, and honest axes.
- [02_Matplotlib](./02_Matplotlib): Figures, axes, styling, annotations, and exports.
- [03_Seaborn_Statistics](./03_Seaborn_Statistics): Distributions, categories, relationships, and uncertainty.
- [04_Plotly_Interactive](./04_Plotly_Interactive): Hover, faceting, filtering, and interactive HTML.
- [05_Data_Storytelling](./05_Data_Storytelling): Questions, comparisons, narratives, and actionable findings.
- [06_Dashboard_Design](./06_Dashboard_Design): KPIs, layouts, visual hierarchy, and accessibility.
- [07_Business_Analytics](./07_Business_Analytics): Revenue, orders, margins, segments, and monthly trends.
- [08_End_to_End_Case_Study](./08_End_to_End_Case_Study): Retail analytics reporting from raw data to executive summary.

## Portfolio integrity
These are guided educational examples. Run each notebook, interpret your outputs, document caveats, and do not claim synthetic findings describe a real business.
