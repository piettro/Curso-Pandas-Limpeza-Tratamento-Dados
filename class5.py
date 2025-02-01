import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_json('Data/data_without_outliers.json')
print(data.info())

mapping = {
    'nao': 0,
    'sim': 1,
    'masculino': 0,
    'feminino': 1
}

columns = ['telefone.servico_telefone', 'Churn', 'cliente.parceiro', 'cliente.dependentes', 'conta.faturamente_eletronico', 'cliente.genero']
data[columns] = data[columns].replace(mapping)
print(data)

for col in data.columns:
    print(f"Coluna: {col}")
    print(data[col].unique())
    print("-" * 30)

df_dummies = pd.get_dummies(data, dtype=int).copy()
print(df_dummies.head())
print(df_dummies.info())

data.to_json('Data/data_clean.json', index=False)