import pandas as pd

def encode_boolean(df, attribute):
    mapping_dict = {'No': 0, 'Yes': 1}
    for att in attribute:
        df[att] = df[att].map(mapping_dict)
    return df

def encode_churn (df):
    df["Churn"] = df["Churn"].astype(int)
    return df