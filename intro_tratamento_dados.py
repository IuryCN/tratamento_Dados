import pandas as pd

df = pd.read_csv('clientes.csv')

#Verficiar os primeiro registros
print(df.head().to_string())

#Verificar os últimos registros
print(df.tail().to_string())

#verficiar quantidade de linhas e colunas
print('Qtd:', df.shape)

#Verificar tipos de dados
print('Tipagem: \n', df.dtypes)

#Verificar valores Nulos
print('Valores Nulos: \n', df.isnull().sum())
