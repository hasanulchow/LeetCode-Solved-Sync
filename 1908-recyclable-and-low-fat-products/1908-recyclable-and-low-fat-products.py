import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    x = products[(products['low_fats'] == 'Y') & (products['recyclable']=='Y')]
    result = x[['product_id']]
    return result