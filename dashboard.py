"""Standalone interactive Plotly dashboard. Run from repository root: python dashboard.py"""
from pathlib import Path
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

path=Path(__file__).parent/'data'/'retail_orders_synthetic.csv'
df=pd.read_csv(path,parse_dates=['order_date'])
df=df[df['status']=='Completed'].copy()
df['net_sales']=df['units']*df['unit_price']*(1-df['discount_rate'])
df['month']=df['order_date'].dt.to_period('M').astype(str)
region=df.groupby('region')['net_sales'].sum().sort_values(ascending=False)
monthly=df.groupby('month')['net_sales'].sum()
fig=make_subplots(rows=1,cols=2,subplot_titles=['Sales by region','Monthly revenue'])
fig.add_trace(go.Bar(x=region.index,y=region.values,name='Region'),row=1,col=1)
fig.add_trace(go.Scatter(x=monthly.index,y=monthly.values,mode='lines+markers',name='Monthly'),row=1,col=2)
fig.update_layout(title=f'Synthetic retail dashboard | Revenue: ${df.net_sales.sum():,.0f} | Completed orders: {len(df)}',height=540)
out=Path(__file__).parent/'retail_dashboard.html'
fig.write_html(str(out),include_plotlyjs=True)
print('Dashboard created:',out)
