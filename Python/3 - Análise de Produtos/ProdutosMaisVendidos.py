import pandas as pd
import matplotlib.pyplot as plt

# Dados das vendas
vendas = [
    {"id": 1, "data": '2023-01-05', "produto": "Banheira", "quantidade": 2, "preco_unitario": 2500.00, "cliente_id": 101},
    {"id": 2, "data": '2023-02-12', "produto": "Ofurô", "quantidade": 1, "preco_unitario": 200.00, "cliente_id": 113},
    
]

# Criando DataFrame das vendas
df_vendas = pd.DataFrame(vendas)

# Agrupando as vendas por produto e somando as quantidades
vendas_por_produto = df_vendas.groupby('produto')['quantidade'].sum()

# Ordenando os produtos pelo total de vendas
vendas_por_produto = vendas_por_produto.sort_values(ascending=False)

# Plotando o gráfico de barras dos produtos mais vendidos
plt.figure(figsize=(10, 6))
vendas_por_produto.plot(kind='bar', color='skyblue')
plt.title('Produtos Mais Vendidos')
plt.xlabel('Produto')
plt.ylabel('Total de Vendas')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
