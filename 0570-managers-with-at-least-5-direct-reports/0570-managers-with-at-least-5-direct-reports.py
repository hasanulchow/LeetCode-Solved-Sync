import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:

    df = employee.groupby('managerId'
                ).size().reset_index(name='idx')

    return df[df.idx >= 5].merge(employee, 
                    left_on='managerId',
                    right_on='id',how='inner').iloc[:,[3]]
   