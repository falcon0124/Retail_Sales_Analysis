
top_customers = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(10)