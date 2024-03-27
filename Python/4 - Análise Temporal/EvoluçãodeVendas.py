import pandas as pd
import matplotlib.pyplot as plt

# Definindo os dados
dados_vendas = [
    {"id": 1, "data": '2023-01-05', "produto": "Banheira", "quantidade": 2, "preco_unitario": 2500.00, "cliente_id": 101},
    {"id": 2, "data": '2023-02-12', "produto": "Ofurô", "quantidade": 1, "preco_unitario": 200.00, "cliente_id": 113},
    
]

# Criando o DataFrame de Vendas
df_vendas = pd.DataFrame(dados_vendas)

# Convertendo a coluna 'data' para o formato datetime
df_vendas['data'] = pd.to_datetime(df_vendas['data'])

# Criando uma nova coluna 'mes' para armazenar o mês da venda
df_vendas['mes'] = df_vendas['data'].dt.to_period('M')

# Agrupando as vendas por mês e somando a quantidade total de vendas
vendas_por_mes = df_vendas.groupby('mes')['quantidade'].sum()

# Plotando o gráfico de linha
plt.figure(figsize=(10, 6))
vendas_por_mes.plot(marker='o', color='green', linestyle='-')
plt.title('Evolução das Vendas ao Longo do Tempo')
plt.xlabel('Mês')
plt.ylabel('Quantidade de Vendas')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
