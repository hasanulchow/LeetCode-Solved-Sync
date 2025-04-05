import pandas as pd

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    ads['clicks'] = np.where(ads['action']=='Clicked',1,0)
    ads['total'] = np.where(ads['action'] != 'Ignored', 1,0)
    df =  ads.groupby(['ad_id'])[['clicks', 'total']].sum().reset_index()
    df['ctr'] = (df['clicks']*100.00/df['total']).round(2).fillna(0)
    return df[['ad_id', 'ctr']].sort_values(by= ['ctr', 'ad_id'], ascending=[False, True])