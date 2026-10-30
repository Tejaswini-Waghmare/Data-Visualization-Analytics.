# Dashboard Design

## Learning objectives
KPIs, layouts, visual hierarchy, and accessibility. You will prepare a reproducible chart, describe the metric and denominator, and identify at least one limitation.

## Analytical workflow
1. Define the business question and target audience.
2. Inspect data grain, missingness, categories, and status values.
3. Restrict to completed transactions before calculating realized sales.
4. Aggregate at the level required by the question.
5. Choose the simplest appropriate chart and label units.
6. Verify totals and category counts against the underlying data.
7. Interpret the chart, quantify differences, and state uncertainty or limitations.

## Essential principles
- **Comparison:** sorted bars; use a common zero baseline for magnitude.
- **Trend:** lines for chronologically ordered values; avoid implying smoothness with sparse observations.
- **Distribution:** histogram for shape, boxplot for median and spread; inspect outliers rather than deleting automatically.
- **Relationship:** scatterplots show association, not causation.
- **Composition:** stacked bars when comparing shares; note that non-baseline segments are harder to compare.
- **Accessibility:** informative titles, axis units, legible fonts, and colorblind-friendly palettes; never rely on color alone.
- **Interactive graphics:** hover is helpful, but static exports should remain interpretable.
- **Responsible reporting:** distinguish synthetic sample results from production metrics; report filtering and exclusions.

## Retail data dictionary
- `order_id`: unique synthetic order identifier.
- `order_date`: transaction date in 2025.
- `region`, `category`, `channel`: categorical dimensions.
- `status`: Completed, Returned, or Cancelled.
- `units`, `unit_price`, `discount_rate`, `cost`: pricing and expense fields.
- `customer_rating`: simulated 1–5 value, not validated feedback.

## Metric formulas
- Gross sales = units × unit price.
- Net sales = gross sales × (1 − discount rate).
- Profit = net sales − cost.
- Margin = profit / net sales (only when denominator is nonzero).
- Average order value = total net sales / number of completed orders.

## Worked examples
### KPI dashboard
```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots
by_region=sales.groupby('region')['net_sales'].sum().sort_values(ascending=False)
by_month=sales.groupby('month')['net_sales'].sum()
fig=make_subplots(rows=1,cols=2,subplot_titles=('Sales by region','Monthly trend'))
fig.add_trace(go.Bar(x=by_region.index,y=by_region.values,name='Region'),row=1,col=1)
fig.add_trace(go.Scatter(x=by_month.index,y=by_month.values,mode='lines+markers',name='Monthly'),row=1,col=2)
fig.update_layout(title=f"Retail dashboard | Revenue ${sales['net_sales'].sum():,.0f} | Orders {len(sales)}",height=480)
fig.show()
```

Explain why this visualization matches the question and how you would check it.

### Filter controls in Python
```python
selected_region='North'
filtered=sales[sales['region'].eq(selected_region)]
print(selected_region, 'revenue:',round(filtered['net_sales'].sum(),2))
print(filtered.groupby('category')['net_sales'].sum().sort_values(ascending=False))
```

Explain why this visualization matches the question and how you would check it.

## Common pitfalls
- Plotting every transaction as a separate category.
- Mixing completed and cancelled orders in sales KPIs.
- Truncating bar chart baselines to exaggerate differences.
- Using averages without showing distributions or counts.
- Claiming a pattern is causal without experimental evidence.

## Further reading
- Matplotlib documentation: https://matplotlib.org/stable/
- Seaborn tutorial: https://seaborn.pydata.org/tutorial.html
- Plotly Python: https://plotly.com/python/
