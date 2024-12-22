# Write your MySQL query statement below
-- Retrieve the second highest salary from the Employee table

SELECT 
    MAX(salary) AS SecondHighestSalary  -- Select the maximum salary from the filtered results, which will be the second highest
FROM 
    Employee 
WHERE 
    salary < (                           -- Only consider salaries less than the highest salary
        SELECT MAX(salary)               -- Subquery to get the highest salary in the Employee table
        FROM Employee
    );
