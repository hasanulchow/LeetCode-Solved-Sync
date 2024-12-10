import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    """
    This function fills missing values in the 'quantity' column of a DataFrame with 0.

    Args:
    products (pd.DataFrame): A DataFrame containing a 'quantity' column with possible missing values.

    Returns:
    pd.DataFrame: The DataFrame with missing values in the 'quantity' column replaced by 0.
    """
    # Replace missing values in the 'quantity' column with 0
    products["quantity"].fillna(0, inplace=True)
    
    # Return the modified DataFrame
    return products
