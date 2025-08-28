
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("HR_Employee.csv")

# Attrition by Department
attr = df.groupby("Department")["Attrition"].apply(lambda x: (x=="Yes").sum())
attr.plot(kind='bar', title='Attrition by Department')
plt.savefig('attrition_by_dept.png')

# Income vs Attrition
income_attr = df.groupby("Attrition")["MonthlyIncome"].mean()
income_attr.plot(kind='bar', title='Income vs Attrition')
plt.savefig('income_vs_attrition.png')
