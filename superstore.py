import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8')
df = pd.read_csv("Sample_Superstore.csv" ,encoding='latin1')

print("null values : ", df.isnull().sum())
print("dups values : ", df.duplicated().sum())

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

print('data typer ', df.dtypes)

#top 10 product by sales

top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_products.values, y=top_products.index, palette="Blues_r")
plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product Name")
plt.show()

#Top selling products by region

region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
plt.figure(figsize=(6,4))
sns.barplot(x=region_sales.index, y=region_sales.values, palette="coolwarm")
plt.title("Total Sales by Region")
plt.ylabel("Sales")
plt.show()

#Sales per financial month

df['Month_Year'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month_Year')['Sales'].sum()

plt.figure(figsize=(12,5))
monthly_sales.plot(kind='line', marker='o', color='teal')
plt.title("Monthly Sales Trend")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

#discount vs profit
plt.figure(figsize=(6,4))
sns.scatterplot(x='Discount', y='Profit', data=df, color='red', alpha=0.5)
plt.title("Discount vs Profit")
plt.show()

#Top 10 coustomers by revenue
top_customers = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(8,5))
sns.barplot(x=top_customers.values, y=top_customers.index, palette="Greens_r")
plt.title("Top 10 Customers by Revenue")
plt.xlabel("Total Sales")
plt.show()

df.to_csv("cleaned_superstore.csv", index=False)
print("Cleaned dataset saved!")
