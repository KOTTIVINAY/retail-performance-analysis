-- Retail Project SQL Analysis (Day 1–3)

-- 1) Monthly Sales Trend (SQLite-friendly using substr)
SELECT substr(Date,1,7) AS Month,
       SUM(Quantity * Price) AS Total_Sales
FROM Retail_Sales
GROUP BY substr(Date,1,7)
ORDER BY Month;

-- 2) Profit by Category
SELECT Category,
       SUM(Profit) AS Total_Profit
FROM Retail_Sales
GROUP BY Category
ORDER BY Total_Profit DESC;

-- 3) Top Selling Products
SELECT Product,
       SUM(Quantity) AS Units_Sold
FROM Retail_Sales
GROUP BY Product
ORDER BY Units_Sold DESC
LIMIT 5;
