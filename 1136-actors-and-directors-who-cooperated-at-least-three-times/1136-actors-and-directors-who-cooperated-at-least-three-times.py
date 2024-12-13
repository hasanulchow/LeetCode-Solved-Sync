import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # Group the data by actor_id and director_id, and count the number of cooperations
    grouped = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='cooperation_count')
    
    # Filter the pairs where the cooperation count is at least three
    filtered_pairs = grouped[grouped['cooperation_count'] >= 3]
    
    return filtered_pairs[['actor_id', 'director_id']]