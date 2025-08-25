import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Retail_Sales.csv")

# Total sales per month
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month').apply(lambda x: (x['Quantity']*x['Price']).sum())

plt.figure(figsize=(8,4))
monthly_sales.plot(kind='bar')
plt.title("Monthly Sales Trend")
plt.ylabel("Total Sales")
plt.savefig("monthly_sales_trend.png")
plt.close()

# Profit by Category
profit_by_cat = df.groupby('Category')['Profit'].sum()

plt.figure(figsize=(6,4))
profit_by_cat.plot(kind='bar', color='orange')
plt.title("Profit by Category")
plt.ylabel("Profit")
plt.savefig("profit_by_category.png")
plt.close()

print("Analysis complete. Charts saved as PNGs.")
