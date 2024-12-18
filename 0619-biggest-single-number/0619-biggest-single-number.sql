# Write your MySQL query statement below

# Select the maximum value from the result set of unique numbers.
SELECT MAX(num) AS num
FROM (
    # Inner query: Retrieve numbers from the `Mynumbers` table
    # that appear only once using GROUP BY and HAVING.
    SELECT num
    FROM Mynumbers
    GROUP BY num
    HAVING COUNT(num) = 1
) AS unique_numbers;
