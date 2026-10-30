# Visualization Fundamentals

## Learning objectives
Choosing chart types, visual encoding, labeling, and honest axes. You will prepare a reproducible chart, describe the metric and denominator, and identify at least one limitation.

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
### Chart selection and comparison
```python
summary = sales.groupby('category',as_index=False)['net_sales'].sum().sort_values('net_sales',ascending=False)
fig, ax = plt.subplots(figsize=(8,4))
ax.bar(summary['category'],summary['net_sales'])
ax.set(title='Completed sales by category',ylabel='Net sales (USD)',xlabel='Category')
plt.tight_layout(); plt.show()
```

Explain why this visualization matches the question and how you would check it.

### Time trends
```python
monthly = sales.groupby('month',as_index=False)['net_sales'].sum()
fig,ax=plt.subplots(figsize=(9,4))
ax.plot(monthly['month'],monthly['net_sales'],marker='o')
ax.set(title='Monthly net sales',ylabel='USD',xlabel='Month')
plt.xticks(rotation=45);plt.tight_layout();plt.show()
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
