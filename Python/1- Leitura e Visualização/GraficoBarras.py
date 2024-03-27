# Terceiro tópico

import pandas as pd
import matplotlib.pyplot as plt

# Definindo os dados
dados_vendas = [
    {'id': 1, 'data': '2023-01-05', 'produto': 'Banheira', 'quantidade': 2, 'preco_unitario': 2500.00, 'cliente_id': 101},
        {'id': 2, 'data': '2023-02-12', 'produto': 'Ofurô', 'quantidade': 1, 'preco_unitario': 200.00, 'cliente_id': 113},
        {'id': 3, 'data': '2023-03-20', 'produto': 'Spa', 'quantidade': 3, 'preco_unitario': 5000.00, 'cliente_id': 103},
]

# Criando o DataFrame de Vendas
df_vendas = pd.DataFrame(dados_vendas)

# Convertendo a coluna 'data' para o formato datetime
df_vendas['data'] = pd.to_datetime(df_vendas['data'])

# Criando uma nova coluna 'mes' para armazenar o mês da venda
df_vendas['mes'] = df_vendas['data'].dt.month

# Agrupando as vendas por mês e contando o número de vendas
vendas_por_mes = df_vendas.groupby('mes').size()

# Plotando o gráfico de barras
#largura de 10 pole. e altura de 6 polegadas
plt.figure(figsize=(10, 6))
#argumento kind='bar' especifica que queremos um gráfico de barras (escolhendo a cor azul)
vendas_por_mes.plot(kind='bar', color='skyblue')
#define o título do gráfico
plt.title('Contagem de Vendas por Mês')
#Define o rótulo do eixo x como 'Mês'
plt.xlabel('Mês')
plt.ylabel('Contagem de Vendas')
#Rotaciona os rótulos do eixo x em 0 graus
plt.xticks(rotation=0)  # Rotaciona os rótulos do eixo x para facilitar a leitura
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
#Exibe o gráfico.
plt.show()