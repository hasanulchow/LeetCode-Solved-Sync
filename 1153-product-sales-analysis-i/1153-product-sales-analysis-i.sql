-- Select the product name, year of sale, and sale price
SELECT 
    Product.product_name, -- Retrieves the name of the product from the Product table
    Sales.year,          -- Retrieves the year of the sale from the Sales table
    Sales.price          -- Retrieves the price of the sale from the Sales table
FROM 
    Product,             -- Specifies the Product table
    Sales               -- Specifies the Sales table
WHERE 
    Product.product_id = Sales.product_id; -- Joins the Product and Sales tables using the product_id column
