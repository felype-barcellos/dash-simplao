import pandas as pd
import numpy as np

# Caminho do arquivo
arquivo = r"C:\Users\felyp\OneDrive\UTFPR  - Curso Analise de Dados\Aula 3\datatran2025.xlsx"

# Leitura do arquivo Excel
df = pd.read_excel(arquivo)

# Exibe as primeiras linhas
print(df.head())

# Informações gerais do DataFrame
print(df.info())

# Estatísticas descritivas para colunas numéricas
print(df.describe())

# Verifica valores ausentes
print(df.isnull().sum())

# Exemplo de análise: contagem de valores únicos por coluna
print(df.nunique())

# Exemplo de análise: correlação entre colunas numéricas
print(df.corr(numeric_only=True))