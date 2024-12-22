
-- Write a query to categorize accounts based on income levels and count them

-- Select the count of accounts with a low salary
SELECT 
    'Low Salary' AS category,                     -- Label this category as 'Low Salary'
    COUNT(IF(income < 20000, 1, NULL)) AS accounts_count -- Count accounts where income is less than 20000
FROM 
    Accounts
UNION ALL
-- Select the count of accounts with an average salary
SELECT 
    'Average Salary',                             -- Label this category as 'Average Salary'
    COUNT(IF(income >= 20000 AND income <= 50000, 1, NULL)) -- Count accounts where income is between 20000 and 50000
FROM 
    Accounts
UNION ALL
-- Select the count of accounts with a high salary
SELECT 
    'High Salary',                                -- Label this category as 'High Salary'
    COUNT(IF(income > 50000, 1, NULL))           -- Count accounts where income is greater than 50000
FROM 
    Accounts;
