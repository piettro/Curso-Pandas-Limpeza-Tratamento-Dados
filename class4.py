import pandas as pd
import json
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_json('Data/data_without_nan.json')
print(data.describe())

Q1 = data['cliente.tempo_servico'].quantile(.25)
Q3 = data['cliente.tempo_servico'].quantile(.75)
IQR = Q3 - Q1
lim_inf = Q1 - 1.5 * IQR
lim_sup = Q3 + 1.5 * IQR

outliers_index = (data['cliente.tempo_servico'] < lim_inf) | (data['cliente.tempo_servico'] > lim_sup)
print(data[outliers_index]['cliente.tempo_servico'])

sns.boxplot(data['cliente.tempo_servico'],orient='h')
plt.show()

df_without_out = data[~outliers_index]
df_without_out.loc[outliers_index, 'cliente.tempo_servico'] = np.ceil(
    df_without_out.loc[outliers_index, 'conta.cobranca.Total'] /
    df_without_out.loc[outliers_index, 'conta.cobranca.mensal']
)

sns.boxplot(df_without_out['cliente.tempo_servico'],orient='h')
plt.show()

df_without_out.to_json('Data/data_without_outliers.json', index=False)