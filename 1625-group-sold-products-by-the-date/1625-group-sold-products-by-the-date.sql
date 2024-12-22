# Write your MySQL query statement below
-- Retrieve the number of distinct products sold and their names for each sell date

SELECT 
    sell_date,                             -- Select the sell date for each transaction
    COUNT(DISTINCT product) AS num_sold,   -- Count the distinct products sold on each sell date
    GROUP_CONCAT(DISTINCT product ORDER BY product) AS products  -- Concatenate the distinct product names sold, ordered by product name
FROM 
    Activities                            -- Specify the table containing the activities
GROUP BY 
    sell_date                             -- Group the results by the sell date
ORDER BY 
    sell_date;                            -- Order the results by the sell date
