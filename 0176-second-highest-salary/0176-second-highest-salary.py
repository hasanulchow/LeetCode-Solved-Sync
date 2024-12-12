import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee['salary'].unique()
    unique_salaries = list(sorted(unique_salaries))
    if len(unique_salaries) > 1:
        return pd.DataFrame({'SecondHighestSalary': [unique_salaries[-2]]})
    else:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    