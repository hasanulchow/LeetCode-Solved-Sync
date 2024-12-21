import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    
    # Step 1: Group employees by 'managerId' and count the number of employees under each manager.
    df = employee.groupby('managerId') \
                 .size() \
                 .reset_index(name='idx')  # 'idx' will store the count of employees for each manager
    
    # Step 2: Filter out managers who have fewer than 5 employees. 
    # Then, merge with the original employee DataFrame to get the manager details.
    return df[df.idx >= 5] \
                .merge(employee,  # Merge on managerId and id to get details of managers.
                       left_on='managerId', 
                       right_on='id', 
                       how='inner') \
                .iloc[:, [3]]  # Select the 4th column (which is the 'name' or 'id' column of the manager)
