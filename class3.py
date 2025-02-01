import pandas as pd
import numpy as np

data = pd.read_json('Data/data_without_churn_empty.json')

#Duplicated Values
print(f'Data duplicated: {data.duplicated().sum()}')
filter_data_duplicated = data.duplicated()
print(data[filter_data_duplicated].head())
data.drop_duplicates(inplace=True)

#NaN Values
print(f'Data with NaN: {data.isna().sum()}')
print(f'Rows with NaN: {data[data.isna().any(axis=1)]}')

data['cliente.tempo_servico'].fillna(
    np.ceil(
        data['conta.cobranca.Total'] / data['conta.cobranca.mensal']
    ), inplace=True
)

#Remove NaN Values
print(data['conta.contrato'].value_counts())

columns_to_drop = ['conta.contrato', 'conta.faturamente_eletronico','conta.metodo_pagamento']
df_withou_nan = data.dropna(subset=columns_to_drop).copy()
df_withou_nan.reset_index(drop=True,inplace=True)

print(df_withou_nan.isna().sum())
df_withou_nan.to_json('Data/data_without_nan.json', index=False)