-- Write your MySQL query statement below

-- Select the rounded sum of `tiv_2016` to two decimal places as the result
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016 
FROM Insurance
WHERE 
    -- Filter rows where `tiv_2015` is present in a subquery
    tiv_2015 IN (
        -- Subquery to find `tiv_2015` values that appear more than once
        SELECT tiv_2015 
        FROM Insurance 
        GROUP BY tiv_2015 
        HAVING COUNT(*) > 1
    )
    AND 
    -- Further filter rows where the combination of `lat` and `lon` appears exactly once
    (lat, lon) IN (
        -- Subquery to find `lat` and `lon` combinations that are unique
        SELECT lat, lon 
        FROM Insurance 
        GROUP BY lat, lon 
        HAVING COUNT(*) = 1
    );
