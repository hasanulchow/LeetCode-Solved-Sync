-- Write your MySQL query statement below

-- Step 1: Create a Common Table Expression (CTE) to calculate the cumulative sum of weights (prefsum)
WITH cte AS (
    SELECT 
        *, 
        SUM(weight) OVER (ORDER BY turn) AS prefsum  -- Calculate the cumulative sum of weight (prefsum) ordered by 'turn'
    FROM Queue
    ORDER BY turn  -- Ensure the rows are ordered by 'turn' before calculating the cumulative sum
)

-- Step 2: Select the person_name with the highest prefsum less than or equal to 1000
SELECT person_name 
FROM cte
WHERE prefsum <= 1000  -- Filter for rows where the cumulative sum is less than or equal to 1000
ORDER BY prefsum DESC   -- Order the results by prefsum in descending order to get the closest person_name
LIMIT 1  -- Limit the result to only the first row (person_name with the highest prefsum <= 1000)

-- Optional Step: Uncomment the next line to view all columns from the CTE
-- SELECT * 
-- FROM cte
