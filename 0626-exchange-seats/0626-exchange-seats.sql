-- Write your MySQL query statement below

-- Step 1: Select the id and apply the CASE statement to determine the student for each row
SELECT id, 

    -- Step 2: Use CASE to handle conditions based on whether the 'id' is even or odd
    CASE
        -- If the 'id' is even (id % 2 = 0), use LAG to get the previous student's value
        WHEN id % 2 = 0 THEN 
            LAG(student) OVER(ORDER BY id)  -- Get the previous student value based on the order of 'id'
        
        -- If the 'id' is odd, use LEAD to get the next student's value, or if NULL, return the current student value
        ELSE 
            COALESCE(LEAD(student) OVER(ORDER BY id), student)  -- Get the next student value, or current student if next is NULL
    END AS student  -- Alias the result of the CASE statement as 'student'

FROM Seat;  -- Query data from the 'Seat' table
