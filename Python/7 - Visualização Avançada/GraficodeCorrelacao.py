import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Definindo os dados
dados_vendas = [
    {"id": 1, "data": '2023-01-05', "produto": "Banheira", "quantidade": 2, "preco_unitario": 2500.00, "cliente_id": 101},
 
]

dados_clientes = [
    {"id": 101, "nome": "João da Silva", "valor_gasto_total": 29000.00},
   
]

# Criando DataFrames
df_vendas = pd.DataFrame(dados_vendas)
df_clientes = pd.DataFrame(dados_clientes)

# Mesclando os DataFrames
df = pd.merge(df_vendas, df_clientes, left_on='cliente_id', right_on='id', how='inner')

# Plotando o gráfico de dispersão
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='quantidade', y='preco_unitario', hue='valor_gasto_total', palette='viridis', size='valor_gasto_total', sizes=(50, 200))
plt.title('Gráfico de Dispersão: Quantidade x Preço Unitário (com Valor Gasto Total)')
plt.xlabel('Quantidade') 
plt.ylabel('Preço Unitário')
plt.legend(title='Valor Gasto Total')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()



# Gráfico de correlação entre variáveis:

# Calculando a matriz de correlação
correlation_matrix = df.corr()

# Plotando o heatmap da matriz de correlação
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Matriz de Correlação entre Variáveis')
plt.show()
