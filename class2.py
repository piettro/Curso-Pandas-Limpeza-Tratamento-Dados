import pandas as pd
import json

data = pd.read_json('Data/data.json')

with open('Data/data.json') as f:
    data_raw = json.load(f)

data_normalize = pd.json_normalize(data_raw)
print(data_normalize.info())

idx_to_update = data_normalize[data_normalize['conta.cobranca.Total'] == ' '].index
data_normalize.loc[idx_to_update, "cliente.tempo_servico"] = 24
data_normalize.loc[idx_to_update, "conta.cobranca.Total"] = data_normalize.loc[idx_to_update, "conta.cobranca.mensal"] * 24

data_normalize['conta.cobranca.Total'] = data_normalize['conta.cobranca.Total'].astype('float64')

for col in data_normalize.columns:
    print(f"Coluna: {col}")
    print(data_normalize[col].unique())
    print("-" * 30)

data_normalize.query("Churn == ''")
data_normalize[data_normalize['Churn'] != '']
data_without_empty = data_normalize[data_normalize['Churn'] != ''].copy()
print(data_without_empty.info())

data_without_empty.reset_index(drop=True, inplace=True)
print(data_without_empty.head())

data_without_empty.to_json('Data/data_clean.json', index=False)