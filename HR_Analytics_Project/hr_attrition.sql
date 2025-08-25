-- HR Analytics - Predict Employee Attrition (Day 1–3)

-- 1) Attrition rate by department
SELECT Department, 
       COUNT(*) AS Total_Employees,
       SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*) AS Attrition_Rate_Percent
FROM HR_Employee
GROUP BY Department;

-- 2) Average income vs attrition
SELECT Attrition, AVG(MonthlyIncome) AS Avg_Income
FROM HR_Employee
GROUP BY Attrition;

-- 3) Attrition by years at company
SELECT YearsAtCompany, 
       SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS Employees_Left
FROM HR_Employee
GROUP BY YearsAtCompany
ORDER BY YearsAtCompany;
