
# 🧼 Análise e Limpeza de Dados com Python

Este projeto tem como objetivo demonstrar técnicas práticas de **limpeza, exploração e tratamento de dados** usando **Pandas**, **NumPy**, **Seaborn**, **Matplotlib** e **Scipy**. A base utilizada contém dados de clientes e o processo envolve desde a inspeção inicial até o tratamento de outliers e inconsistências.

---

## 📁 Estrutura dos Scripts

### 🔍 1. Visualização Inicial dos Dados
**Simulado dentro do repositório (sem script separado)**  
Lê o dataset original e realiza inspeções básicas:

```python
import pandas as pd

df = pd.read_csv('clientes.csv')

# Ver primeiros registros
print(df.head().to_string())

# Ver últimos registros
print(df.tail().to_string())

# Ver dimensões
print('Qtd:', df.shape)

# Ver tipos de dados
print('Tipagem: \n', df.dtypes)

# Ver valores nulos
print('Valores Nulos: \n', df.isnull().sum())
```

---

### 🧽 2. Limpeza de Dados
**Arquivo:** `limpeza_dados.py`

- Remoção de colunas e valores inconsistentes
- Normalização de strings
- Preenchimento de dados ausentes

---

### ⚠️ 3. Identificação de Inconsistências
**Arquivo:** `inconsistencias.py`

- Filtra e lista registros com:
  - Endereços curtos ou ausentes
  - Nomes com caracteres inválidos
  - CPFs mal formatados

---

### 📊 4. Estudo com Lambda Functions
**Arquivo:** `estudo_lambda.py`

- Aplica funções `lambda` para limpeza e transformação de strings
- Demonstra como manipular texto de forma funcional

---

### 🚨 5. Tratamento de Outliers
**Arquivo:** `outliers.py`

Este script identifica e remove outliers no campo **'idade'** utilizando dois métodos estatísticos:

#### ✅ Z-Score:
- Remove valores com desvio superior a 3

#### ✅ IQR (Intervalo Interquartil):
- Remove valores abaixo do Q1 - 1.5×IQR ou acima do Q3 + 1.5×IQR

Também trata:
- Endereços com formato inválido (menos de 3 linhas)
- Nomes com mais de 20 caracteres como "Nome inválido"

No final, os dados são salvos em um novo arquivo `.csv` com os outliers removidos.

---

## 🛠 Bibliotecas Utilizadas

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scipy`

---

## 📁 Saídas Geradas

- `clientes_limpeza.csv` — Após a primeira etapa de limpeza
- `clientes_limpeza_outliers.csv` — Após remoção de outliers e tratamento textual

---

## 👨‍💻 Autor

**Iury Nolasco**  
Estudante de Ciência de Dados | Apaixonado por Python & análise exploratória  
Abril/2025
