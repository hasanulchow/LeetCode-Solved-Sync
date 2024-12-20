# Write your MySQL query statement below
-- Select x, y, z, and evaluate whether they can form a triangle
SELECT 
    x, 
    y, 
    z, 
    -- Check the triangle condition using a CASE statement
    CASE 
        -- If the sum of any two sides is greater than the third side
        WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'
        -- Otherwise, it's not a triangle
        ELSE 'No'  
    END AS triangle
FROM 
    Triangle;
