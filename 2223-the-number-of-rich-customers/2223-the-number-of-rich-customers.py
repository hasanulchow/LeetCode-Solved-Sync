import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    df = store[store['amount'] > 500]
    count = df['customer_id'].nunique()
    result_df = pd.DataFrame({'rich_count':[count]})
    return result_df