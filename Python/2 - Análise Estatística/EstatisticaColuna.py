# Importando a biblioteca pandas
import pandas as pd

# Dados de vendas
vendas_data = [
    {"id": 1, "data": '2023-01-05', "produto": "Banheira", "quantidade": 2, "preco_unitario": 2500.00, "cliente_id": 101},
    {"id": 2, "data": '2023-02-12', "produto": "Ofurô", "quantidade": 1, "preco_unitario": 200.00, "cliente_id": 113},  
]

# Criando o DataFrame de vendas
df_vendas = pd.DataFrame(vendas_data)

# Calculando estatísticas descritivas básicas
estatisticas_descritivas_numericas = df_vendas.describe()

# Calculando estatísticas descritivas básicas para colunas não numéricas
estatisticas_descritivas_nao_numericas = df_vendas.describe(include='object')

# Mostrando as estatísticas descritivas para colunas numéricas
print("Estatísticas descritivas básicas para as colunas numéricas do DataFrame de vendas:")
print(estatisticas_descritivas_numericas)

# Mostrando as estatísticas descritivas para colunas não numéricas
print("\nEstatísticas descritivas básicas para as colunas não numéricas do DataFrame de vendas:")
print(estatisticas_descritivas_nao_numericas)
