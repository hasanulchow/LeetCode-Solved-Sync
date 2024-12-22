-- Format names with the first letter in uppercase and the rest in lowercase
SELECT 
    user_id, 
    -- Use CONCAT to combine the uppercase first letter and the lowercase rest of the string
    CONCAT(
        UPPER(SUBSTR(name, 1, 1)),        -- Extract the first character and convert it to uppercase
        LOWER(SUBSTR(name, 2, LENGTH(name))) -- Extract the rest of the name starting from the second character and convert it to lowercase
    ) AS name
FROM 
    Users
ORDER BY 
    user_id;                             -- Sort the result by user_id
