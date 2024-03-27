import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Dados de vendas convertidos para estrutura de dados Python
dados_vendas = [
    {"id": 1, "data": '2023-01-05', "produto": "Banheira", "quantidade": 2, "preco_unitario": 2500.00, "cliente_id": 101},
    {"id": 2, "data": '2023-02-12', "produto": "Ofurô", "quantidade": 1, "preco_unitario": 200.00, "cliente_id": 113},

]

# Dados de vendas convertidos para DataFrame
df_vendas = pd.DataFrame(dados_vendas)

# Convertendo a coluna 'data' para datetime
df_vendas['data'] = pd.to_datetime(df_vendas['data'])

# Calculando a receita total por mês
df_vendas['receita'] = df_vendas['quantidade'] * df_vendas['preco_unitario']
receita_por_mes = df_vendas.groupby(df_vendas['data'].dt.to_period('M'))['receita'].sum()

# Plotando o gráfico de linha da receita total ao longo do tempo
plt.figure(figsize=(12, 6))
receita_por_mes.plot(marker='o', linestyle='-')
plt.title('Receita Total ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Receita Total (R$)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Decomposição de séries temporais para identificar padrões sazonais
resultados_decomposicao = seasonal_decompose(receita_por_mes, model='multiplicative')
resultados_decomposicao.plot()
plt.suptitle('Decomposição de Séries Temporais')
plt.show()
