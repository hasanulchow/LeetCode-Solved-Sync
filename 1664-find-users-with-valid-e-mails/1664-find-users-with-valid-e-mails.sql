# Write your MySQL query statement below
-- Retrieve all users whose email matches the specified pattern

SELECT * 
FROM Users                           -- Select all columns from the Users table
WHERE mail REGEXP                    -- Filter the rows based on the email pattern using REGEXP (regular expression)
    '^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode(\\?com)?\\.com$';  -- Regular expression pattern to match valid emails
