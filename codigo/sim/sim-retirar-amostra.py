import pandas as pd
import csv

dados = pd.read_csv('Mortalidade_Geral_2021.csv', sep=';', quotechar='"', dtype=str)

amostra = dados.sample(n=50000, random_state=42)

# amostra.to_csv('Mortalidade_2021_Amostra.csv', index=False, quotechar='"', doublequote=False, escapechar='\\')

amostra.to_csv(
    'Mortalidade_2021_Amostra.csv',
    sep=';',
    index=False,
    quoting=csv.QUOTE_NOTNULL,  # <- Força aspas em todos os campos
    quotechar='"'
)


