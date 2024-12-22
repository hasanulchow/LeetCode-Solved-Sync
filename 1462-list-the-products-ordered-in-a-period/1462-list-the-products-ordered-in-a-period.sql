-- Write your MySQL query statement below

-- Select the product name and the total units sold for the desired result
SELECT 
    p.product_name AS product_name, -- Get the product name from the Products table
    SUM(o.unit) AS unit            -- Calculate the total units sold for each product
FROM 
    Products p                     -- Alias for the Products table
JOIN 
    Orders o                       -- Alias for the Orders table
    USING (product_id)             -- Join condition: Match rows based on product_id
WHERE 
    YEAR(o.order_date) = '2020'    -- Filter orders from the year 2020
    AND MONTH(o.order_date) = '02' -- Further filter orders to only include February
GROUP BY 
    p.product_id                   -- Group the results by product_id (unique products)
HAVING 
    SUM(o.unit) >= 100;            -- Include only those products with total units sold >= 100
