"""
outliers.py

Este script identifica e remove outliers no campo 'idade' do dataset usando dois métodos:
- Z-score (desvio padrão)
- IQR (Intervalo Interquartil)

Autor: Iury Nolasco
Data: Abril/2025
"""


import pandas as pd
from scipy import stats

pd.set_option('display.width', None)
df = pd.read_csv('clientes_limpeza.csv')

# Identificar Outliers com Z-score
z_scores = stats.zscore(df['idade'].dropna())  # Cálculo correto do Z-score
outliers_z = df[(z_scores >= 3) | (z_scores <= -3)]  # Identificar apenas os outliers com Z > 3 ou Z < -3
print('\n===== OUTLIERS POR Z-SCORE =====\n', outliers_z)

# Filtrar os valores que estão dentro da faixa aceitável (-3 <= Z-score <= 3)
df_zscore = df[(-3 <= z_scores) & (z_scores <= 3)]  # Filtro que remove os outliers
print('\n===== DADOS SEM OUTLIERS (Z-SCORE) =====\n', df_zscore)


#Identificar outliers com IQR
Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

limite_baixo = Q1 - 1.5 * IQR
limite_alto = Q3 + 1.5 * IQR
print('Limites IQR:', limite_baixo, limite_alto)

outliers_iqr = df[(df['idade'] < limite_baixo) | (df['idade'] > limite_alto)]
print('\n===== OUTLIERS POR IQR =====\n', outliers_iqr)


#Filtrar outlier com IQR
df_iqr = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]
limite_baixo = 18
limite_alto = 98
df = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]

#Filtrar endereços inválidos
df['endereco'] = df['endereco'].apply(lambda x:'endereco inválido' if len(x.split('\n')) < 3 else x)
print('Qtd de registros com nomes grande:', (df['endereco'] == 'Endereco inválido').sum())
#Tratar campos de texto
df['nome'] = df['nome'].apply(lambda x: 'Nome inválido' if isinstance(x,str) and len(x) > 20 else x)
print('Qtd de registros com nomes grandes: ',(df['nome'] == 'Nome inválido').sum())

print('\n===== DADOS SEM OUTLIERS (IQR) =====\n', df_iqr)

#salvar dataframe
df.to_csv('clientes_limpeza_outliers.csv', index=False)

