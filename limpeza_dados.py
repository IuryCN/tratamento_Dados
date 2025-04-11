import pandas as pd  # Importa a biblioteca pandas para manipulação de dados

# ======== LEITURA DO CSV ========
df = pd.read_csv('clientes.csv')  # Lê o arquivo CSV com os dados dos clientes
pd.set_option('display.max_rows', None)
print(df.head())

# Exibir todas as colunas
pd.set_option('display.max_columns', None)

# Ajustar largura da exibição no console
pd.set_option('display.width', 975)

# ======== REMOÇÃO DE COLUNA 'pais' (se existir) ========
if 'pais' in df.columns:
    df.drop('pais', axis=1, inplace=True)
else:
    print("Aviso: A coluna 'pais' não existe no DataFrame.")

# ======== NORMALIZAÇÃO DE TEXTO ========
df['nome'] = df['nome'].str.title()
df['endereco'] = df['endereco'].str.lower()
df['estado'] = df['estado'].str.strip().str.upper()

# ======== CONVERSÃO DE IDADE ========
if 'idade' in df.columns:
    df['idade'] = pd.to_numeric(df['idade'], errors='coerce')  # Converte idade para numérico (NaNs se erro)
    df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean()).astype(int)  # Corrige NaN com média
else:
    print("Coluna 'idade' não encontrada!")

# ======== TRATAMENTO DE VALORES NULOS ========
df = df.dropna(subset=['cpf'])  # Remove linhas onde o CPF está ausente

# Preenche valores personalizados
df['estado'] = df['estado'].fillna('DESCONHECIDO')
df['endereco'] = df['endereco'].fillna('Endereço não informado')

# ======== CONVERSÃO E FORMATAÇÃO DE DATA ========
if 'data' in df.columns:
    df['data_corrigida'] = pd.to_datetime(df['data'], errors='coerce')  # Converte para datetime
    df['data'] = df['data_corrigida'].dt.strftime('%d/%m/%Y')  # Formata ao estilo BR
else:
    print("Coluna 'data' não encontrada!")

# ======== REMOÇÃO DE DUPLICATAS ========
print('Qtd registros antes:', df.shape[0])
df.drop_duplicates(subset='cpf', inplace=True)
print('Qtd registros após remover duplicatas:', df.shape[0])

# ======== ATUALIZAÇÕES FINAIS E SALVAMENTO ========
df['idade'] = df['idade_corrigida']  # Substitui a coluna idade pela corrigida

# Define as colunas que serão salvas
df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco', 'estado']]
df_salvar.to_csv('clientes_limpeza.csv', index=False)

# Exibe o novo arquivo gerado
print('Novo DataFrame salvo:\n', pd.read_csv('clientes_limpeza.csv'))
