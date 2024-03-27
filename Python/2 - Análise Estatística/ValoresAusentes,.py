import pandas as pd

# Definindo os dados de vendas, comportamento do cliente e desempenho do produto
dados_vendas = [
    {"id": 1, "data": '2023-01-05', "produto": "Banheira", "quantidade": 2, "preco_unitario": 2500.00, "cliente_id": 101},
    {"id": 2, "data": '2023-02-12', "produto": "Ofurô", "quantidade": 1, "preco_unitario": 200.00, "cliente_id": 113},
 
]

dados_comportamento_cliente = [
    {"id": 101, "nome": "João da Silva", "idade": 45, "sexo": "Masculino", "cidade": "São Paulo", "valor_gasto_total": 29000.00},
    {"id": 102, "nome": "Maria Oliveira", "idade": 38, "sexo": "Feminino", "cidade": "Rio de Janeiro", "valor_gasto_total": 30800.00},
 
]

dados_desempenho_produto = [
    {"produto": "Banheira", "vendas_totais": "26 unidades", "receita_total": 65000.00},
    {"produto": "Ofurô", "vendas_totais": "22 unidades", "receita_total": 37200.00},
 
]

# Criando DataFrames
df_vendas = pd.DataFrame(dados_vendas)
df_comportamento_cliente = pd.DataFrame(dados_comportamento_cliente)
df_desempenho_produto = pd.DataFrame(dados_desempenho_produto)

# Verificando se há valores ausentes nos DataFrames
print("Valores ausentes em df_vendas:")
print(df_vendas.isnull().sum())

print("\nValores ausentes em df_comportamento_cliente:")
print(df_comportamento_cliente.isnull().sum())

print("\nValores ausentes em df_desempenho_produto:")
print(df_desempenho_produto.isnull().sum())
