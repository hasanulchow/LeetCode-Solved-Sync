-- Write your MySQL query statement below

-- Step 1: Create a Common Table Expression (CTE) to rank products by change_date within each product_id
WITH cte AS (
    SELECT 
        *, 
        RANK() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS r  -- Rank products based on change_date in descending order
    FROM Products
    WHERE change_date <= '2019-08-16'   -- Filter products with change_date on or before '2019-08-16'
)

-- Step 2: Select the latest price for each product from the CTE
SELECT 
    product_id, 
    new_price AS price                    -- Select the new price from the CTE where the rank is 1 (latest)
FROM cte
WHERE r = 1

-- Step 3: Select default price for products that have no changes up to '2019-08-16'
UNION

SELECT 
    product_id, 
    10 AS price                           -- Assign a default price of 10 for products with no record in the CTE
FROM Products
WHERE product_id NOT IN (SELECT product_id FROM cte)   -- Filter products that don't exist in the CTE
