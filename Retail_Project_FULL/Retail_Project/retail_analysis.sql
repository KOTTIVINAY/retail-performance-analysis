
-- Retail Project SQL Queries
SELECT strftime('%m-%Y', Date) as Month, SUM(Sales) as Total_Sales
FROM Retail_Sales
GROUP BY Month;

SELECT Category, SUM(Profit) as Total_Profit
FROM Retail_Sales
GROUP BY Category;
