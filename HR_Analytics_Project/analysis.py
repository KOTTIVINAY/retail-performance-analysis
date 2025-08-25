import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("HR_Employee.csv")

# Attrition by Department
attrition_dept = df.groupby('Department')['Attrition'].apply(lambda x: (x=='Yes').sum())

plt.figure(figsize=(6,4))
attrition_dept.plot(kind='bar', color='red')
plt.title("Attrition by Department")
plt.ylabel("Employees Left")
plt.savefig("attrition_by_dept.png")
plt.close()

# Income vs Attrition
income_attr = df.groupby('Attrition')['MonthlyIncome'].mean()

plt.figure(figsize=(5,4))
income_attr.plot(kind='bar', color='green')
plt.title("Average Income vs Attrition")
plt.ylabel("Avg Monthly Income")
plt.savefig("income_vs_attrition.png")
plt.close()

print("HR Analysis complete. Charts saved as PNGs.")
