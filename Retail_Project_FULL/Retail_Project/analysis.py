
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Retail_Sales.csv")

# Monthly sales trend
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()
monthly_sales.plot(kind='bar', title='Monthly Sales Trend')
plt.savefig('monthly_sales_trend.png')

# Profit by Category
profit_by_cat = df.groupby('Category')['Profit'].sum()
profit_by_cat.plot(kind='bar', title='Profit by Category')
plt.savefig('profit_by_category.png')
