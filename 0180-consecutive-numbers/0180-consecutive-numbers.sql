-- Write your MySQL query statement below

-- Step 1: Create a Common Table Expression (CTE) to calculate consecutive numbers
WITH CTE AS (
    SELECT 
        num,                                -- Current row's number
        LEAD(num, 1) OVER() AS num1,       -- Number from the next row
        LEAD(num, 2) OVER() AS num2        -- Number from two rows ahead
    FROM logs                              -- Source table
)

-- Step 2: Select unique numbers that appear at least three times consecutively
SELECT DISTINCT 
    num AS ConsecutiveNums                -- Output the number that appears consecutively
FROM CTE
WHERE 
    num = num1 AND                         -- Check if the current number matches the next row's number
    num = num2;                            -- Check if the current number matches two rows ahead
