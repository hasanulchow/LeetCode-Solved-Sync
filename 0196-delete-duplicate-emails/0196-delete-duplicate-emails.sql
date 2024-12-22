# Write your MySQL query statement below
-- Delete duplicate records from the Person table based on the email field

DELETE FROM Person 
-- Specify the table from which the records will be deleted

WHERE id IN (
    -- Subquery to identify records with duplicate emails
    SELECT a.id
    FROM (
        -- Inner subquery to generate row numbers for each email group
        SELECT id, email, 
               ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn
        FROM Person
    ) a
    WHERE a.rn > 1  -- Select only the rows where the row number is greater than 1 (duplicates)
);
