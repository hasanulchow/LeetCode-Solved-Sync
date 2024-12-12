import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    # Group the activities by sell_date and collect the unique products for each date
    grouped = activities.groupby('sell_date')['product'].agg(['nunique', lambda x: ','.join(sorted(set(x)))]).reset_index()
    
    # Rename the columns for clarity
    grouped.columns = ['sell_date', 'num_sold', 'products']
    
    # Replace variations of 'Mask' with just 'Mask'
    grouped['products'] = grouped['products'].str.replace(r'(^|,)Mask(,|$)', r'\1Mask\2')
    
    # Sort the result table by sell_date
    result = grouped.sort_values(by='sell_date')
    
    return result