-- Select the customer ID and the count of visits where no transactions occurred
SELECT 
    V.Customer_id,              -- Retrieves the customer ID from the Visits table
    COUNT(V.visit_id) AS count_no_trans -- Counts the number of visits without transactions and labels it as count_no_trans
FROM 
    Visits V                   -- Alias V refers to the Visits table
LEFT JOIN 
    Transactions T             -- Perform a LEFT JOIN with the Transactions table
ON 
    V.Visit_id = T.Visit_id    -- Join condition to match visits with their corresponding transactions
WHERE 
    T.transaction_id IS NULL   -- Filters only visits that have no matching transactions
GROUP BY 
    V.customer_id;             -- Groups the results by customer ID
