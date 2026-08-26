import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    return person.merge(right=address, how='left')[['lastName', 'firstName', 'city', 'state']]