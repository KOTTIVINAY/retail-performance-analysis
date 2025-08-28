
-- HR Project SQL Queries
SELECT Department, COUNT(*) as Total_Employees, SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) as Attrition_Count
FROM HR_Employee
GROUP BY Department;

SELECT Attrition, AVG(MonthlyIncome) as Avg_Income
FROM HR_Employee
GROUP BY Attrition;
