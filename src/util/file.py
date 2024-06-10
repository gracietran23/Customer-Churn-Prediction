import pandas as pd

def read_data(file_path, **kwargs):
    return pd.read_csv(file_path, **kwargs)
