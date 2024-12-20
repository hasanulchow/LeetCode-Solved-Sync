# Write your MySQL query statement below
-- Select the employee_id and department_id from the Employee table
SELECT employee_id, department_id
FROM Employee
WHERE 
    -- Include rows where the primary_flag is 'Y'
    primary_flag = 'Y' 
    OR 
    -- Include rows where the employee has only one record in the table
    employee_id IN (
        SELECT employee_id
        FROM Employee
        -- Group the data by employee_id to count the number of records per employee
        GROUP BY employee_id
        -- Filter to include only those employees with exactly one record
        HAVING COUNT(employee_id) = 1
    );
