import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    """
    This function finds customers who have not placed any orders.
    
    Args:
    customers (pd.DataFrame): A DataFrame containing customer details with at least columns 'id' and 'name'.
    orders (pd.DataFrame): A DataFrame containing order details with at least a column 'customerId'.
    
    Returns:
    pd.DataFrame: A DataFrame with a single column 'Customers' listing the names of customers who have not placed orders.
    """
    # Filter customers whose 'id' is not present in the 'customerId' column of the orders DataFrame
    df = customers[~customers['id'].isin(orders['customerId'])]

    # Select only the 'name' column and rename it to 'Customers'
    df = df[['name']].rename(columns={'name': 'Customers'})

    # Return the resulting DataFrame
    return df
