'''Usando as bibliotecas Pandas e MatPlotLib e um dataset (podes selecionar das aulas, fazer
download na plataforma kaggle ou escolher um dataset pessoal), elabora um notebook
jupyter no qual efetues:
• Limpeza e tratamento de dados;
Processamento de dados: groupby, filter, criação de novas colunas,…;
• Visualização de dados;'''


import pandas as pd
import matplotlib.pyplot as plt

# Carregar dataset (substituir pelo caminho do seu dataset)
df = pd.read_csv('seu_dataset.csv')

# Exibir primeiras linhas
display(df.head())

# Limpeza de dados: remover valores nulos
df = df.dropna()

# Criar uma nova coluna baseada em uma existente
df['Nova_Coluna'] = df['Coluna_Existente'] * 2

# Agrupar dados por uma coluna específica
grouped_data = df.groupby('Categoria').mean()

# Filtrar dados conforme uma condição
filtered_data = df[df['Valor'] > 10]

# Visualização de dados
plt.figure(figsize=(8,5))
plt.bar(grouped_data.index, grouped_data['Valor'])
plt.xlabel('Categoria')
plt.ylabel('Média do Valor')
plt.title('Média dos Valores por Categoria')
plt.show()

# Exibir dataset processado
display(df.head())
