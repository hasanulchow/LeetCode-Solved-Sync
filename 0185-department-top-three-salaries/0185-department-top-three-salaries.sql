# Write your MySQL query statement below
-- Select the department name, employee name, and salary for the desired result
SELECT 
    d.name AS department,          -- Get the department name from the Department table
    e1.name AS employee,           -- Get the employee name from the Employee table
    e1.salary AS salary            -- Get the salary of the employee
FROM 
    Employee e1                    -- Alias for the Employee table
JOIN 
    Department d                   -- Alias for the Department table
    ON e1.DepartmentId = d.Id      -- Join condition: Match Employee's DepartmentId with Department's Id
WHERE 
    -- Condition to find the top 3 highest salaries in each department
    3 > (
        -- Subquery to count how many distinct salaries are greater than the current employee's salary
        SELECT COUNT(DISTINCT e2.Salary) 
        FROM Employee e2           -- Another alias for the Employee table
        WHERE 
            e2.Salary > e1.Salary  -- Find employees with a higher salary than the current employee
            AND e1.DepartmentId = e2.DepartmentId -- Only consider employees in the same department
    );
