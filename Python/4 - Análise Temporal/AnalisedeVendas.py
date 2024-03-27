import pandas as pd
import matplotlib.pyplot as plt

# Definindo os dados das vendas
dados_vendas = [
    {"id": 1, "data": '2023-01-05', "produto": "Banheira", "quantidade": 2, "preco_unitario": 2500.00, "cliente_id": 101},
    {"id": 2, "data": '2023-02-12', "produto": "Ofurô", "quantidade": 1, "preco_unitario": 200.00, "cliente_id": 113},

]

# Criando o DataFrame de Vendas
df_vendas = pd.DataFrame(dados_vendas)

# Convertendo a coluna 'data' para o formato datetime
df_vendas['data'] = pd.to_datetime(df_vendas['data'])

# Criando uma nova coluna 'mes' para armazenar o mês da venda
df_vendas['mes'] = df_vendas['data'].dt.month

# Calculando a receita total por mês
df_vendas['receita'] = df_vendas['quantidade'] * df_vendas['preco_unitario']
receita_por_mes = df_vendas.groupby('mes')['receita'].sum()

# Plotando o gráfico de linha
plt.figure(figsize=(10, 6))
plt.plot(receita_por_mes.index, receita_por_mes.values, marker='o', color='blue', linestyle='-')
plt.title('Receita Total por Mês')
plt.xlabel('Mês')
plt.ylabel('Receita Total (R$)')
plt.xticks(receita_por_mes.index)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
