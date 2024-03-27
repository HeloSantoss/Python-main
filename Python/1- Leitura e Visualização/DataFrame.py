import pandas as pd

# Definição dos dados em um dicionário
dados = {
    'vendas': [
        {'id': 1, 'data': '2023-01-05', 'produto': 'Banheira', 'quantidade': 2, 'preco_unitario': 2500.00, 'cliente_id': 101},
        {'id': 2, 'data': '2023-02-12', 'produto': 'Ofurô', 'quantidade': 1, 'preco_unitario': 200.00, 'cliente_id': 113},
        {'id': 3, 'data': '2023-03-20', 'produto': 'Spa', 'quantidade': 3, 'preco_unitario': 5000.00, 'cliente_id': 103},
    ],
    'comportamento_do_cliente': [
        {'id': 101, 'nome': 'João da Silva', 'idade': 45, 'sexo': 'Masculino', 'cidade': 'São Paulo', 'valor_gasto_total': 29000.00},
        {'id': 102, 'nome': 'Maria Oliveira', 'idade': 38, 'sexo': 'Feminino', 'cidade': 'Rio de Janeiro', 'valor_gasto_total': 30800.00},
        {'id': 103, 'nome': 'Carlos Souza', 'idade': 50, 'sexo': 'Masculino', 'cidade': 'Belo Horizonte', 'valor_gasto_total': 30000.00},
    ],
    'desempenho_do_produto': [
        {'produto': 'Banheira', 'vendas_totais': 26, 'receita_total': 65000.00},
        {'produto': 'Ofurô', 'vendas_totais': 22, 'receita_total': 37200.00},
        {'produto': 'Spa', 'vendas_totais': 21, 'receita_total': 105000.00},
    ]
}

# Criar DataFrames para cada seção
df_vendas = pd.DataFrame(dados['vendas'])
df_clientes = pd.DataFrame(dados['comportamento_do_cliente'])
df_desempenho_produto = pd.DataFrame(dados['desempenho_do_produto'])

# Exibir os primeiros registros de cada DataFrame
print("DataFrame de Vendas:")
print(df_vendas.head())
print("\nDataFrame de Clientes:")
print(df_clientes.head())
print("\nDataFrame de Desempenho do Produto:")
print(df_desempenho_produto.head())
