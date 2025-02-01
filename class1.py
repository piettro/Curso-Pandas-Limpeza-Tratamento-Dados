import pandas as pd
import json

data = pd.read_json('Data/data.json')

with open('Data/data.json') as f:
    data_raw = json.load(f)
    print(data_raw)

data_normalize = data.json_normalize(data_raw)

print(data_normalize.head())