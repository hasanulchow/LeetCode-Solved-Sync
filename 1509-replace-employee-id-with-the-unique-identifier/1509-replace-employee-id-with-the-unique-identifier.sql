# Write your MySQL query statement below
SELECT
employeeUNI.unique_id, Employees.name
FROM Employees
LEFT JOIN EmployeeUNI on Employees.id = EmployeeUNI.id
