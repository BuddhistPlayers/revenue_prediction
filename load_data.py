import json
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize

JSON_COLUMNS = ['device', 'geoNetwork', 'totals', 'trafficSource']
df = pd.read_csv('C:/Users/sunshine/Desktop/train.csv',
                     converters={column: json.loads for column in JSON_COLUMNS},
                     dtype={'fullVisitorId': 'str'},
                     nrows=None)

for column in JSON_COLUMNS:
    c1 = np.array(df[column])
    c2 = c1.tolist()
    column_as_df = json_normalize(c2)
    column_as_df.columns = [f"{column}.{subcolumn}" for subcolumn in column_as_df.columns]
    df = df.drop(column, axis=1).merge(column_as_df, right_index=True, left_index=True)


df.to_csv('C:/Users/sunshine/Desktop/oridata.csv')
