# Write your MySQL query statement below

SELECT 
    * 
FROM 
    Cinema
WHERE
    MOD(id, 2) = 1 -- Select rows where the `id` is odd
    AND description != 'boring' -- Exclude rows where the `description` is 'boring'
ORDER BY 
    rating DESC; -- Sort the results by `rating` in descending order
