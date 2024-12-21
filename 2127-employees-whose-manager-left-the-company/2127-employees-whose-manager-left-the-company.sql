-- Write your MySQL query statement below

-- Step 1: Select employee_id from the employees table where salary is less than 30000
SELECT employee_id 
FROM employees
WHERE salary < 30000  -- Filter employees whose salary is less than 30,000

-- Step 2: Ensure that the employee's manager_id is not in the list of employee_ids from the employees table
AND manager_id NOT IN (
    SELECT employee_id FROM employees  -- Select all employee_ids from employees table to exclude from manager_id
)

-- Step 3: Order the result by employee_id
ORDER BY employee_id;  -- Order the result in ascending order of employee_id
