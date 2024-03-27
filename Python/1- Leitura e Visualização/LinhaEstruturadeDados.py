# Segundo tópico
import pandas as pd

# Definindo os dados
dados_vendas = [
{"id": 1, "data": '2023-01-05', "produto": "Banheira", "quantidade": 2, "preco_unitario": 2500.00, "cliente_id": 101},
{"id": 2, "data": '2023-02-12', "produto": "Ofurô", "quantidade": 1, "preco_unitario": 200.00, "cliente_id": 113},
{"id": 3,"data": '2023-03-20', "produto": "Spa", "quantidade": 3,"preco_unitario": 5000.00,     "cliente_id": 103}, 
{"id": 4,"data": '2023-04-10',"produto": "Banheira","quantidade": 1,"preco_unitario": 2500.00,"cliente_id": 104},
{"id": 5,"data": '2023-05-15',"produto": "Ofurô","quantidade": 2, "preco_unitario": 250.00, "cliente_id": 105},
{"id": 6,"data": '2023-06-25',"produto": "Spa","quantidade": 2, "preco_unitario": 5000.00,"cliente_id": 106},
{"id": 7,"data": '2023-07-05'," produto": "Banheira","quantidade": 1,"preco_unitario": 2500.00,"cliente_id": 113},
{ "id": 8,"data": '2023-08-18',"produto": "Ofurô","quantidade": 3,"preco_unitario": 500.00,"cliente_id": 108},
{"id": 9,"data": '2023-09-30',"produto": "Spa","quantidade": 1,"preco_unitario": 5000.00,"cliente_id": 109},
{"id": 10,"data": '2023-10-08',"produto": "Banheira","quantidade": 2,"preco_unitario": 2500.00,"cliente_id": 110},
{"id": 11,"data": '2023-11-12',"produto": "Ofurô","quantidade": 1,"preco_unitario": 1000.00,"cliente_id": 111},
{"id": 12,"data": '2023-12-20',"produto": "Spa","quantidade": 3,"preco_unitario": 5000.00,"cliente_id": 112},
{"id": 13,"data": '2023-01-05',"produto": "Banheira","quantidade": 3,"preco_unitario": 2500.00,"cliente_id": 101},
{"id": 14,"data": '2023-02-12',"produto": "Ofurô","quantidade": 1,"preco_unitario": 9000.00,"cliente_id": 102},
{"id": 15,"data": '2023-03-20',"produto": "Spa","quantidade": 2,"preco_unitario": 5000.00,"cliente_id": 103},
{"id": 16,"data": '2023-04-10', "produto": "Banheira","quantidade": 2,"preco_unitario": 2500.00,"cliente_id": 104},
{"id": 17,"data": '2023-05-15'," produto":" Ofurô","quantidade": 3,"preco_unitario": 200.00,"cliente_id": 105},
{"id": 18,"data": '2023-06-25',"produto": "Spa","quantidade": 1,"preco_unitario": 5000.00,"cliente_id": 106},
{"id": 26, "data": '2023-02-12', "produto": "Ofurô", "quantidade": 3, "preco_unitario": 800.00, "cliente_id": 102},
{"id": 27, "data": '2023-03-20', "produto": "Spa", "quantidade": 1, "preco_unitario": 5000.00, "cliente_id": 103},
{"id": 51, "data": '2023-03-20', "produto": "Spa", "quantidade": 1, "preco_unitario": 5000.00, "cliente_id": 103},
{"id": 52, "data": '2023-04-10', "produto": "Banheira", "quantidade": 1, "preco_unitario": 2500.00, "cliente_id": 113},
{"id": 53, "data": '2023-05-15', "produto": "Ofurô", "quantidade": 2, "preco_unitario": 100.00, "cliente_id": 105},
   
    
]

dados_comportamento_cliente = [
    {"id": 101, "nome": "João da Silva", "idade": 45, "sexo": "Masculino", "cidade": "São Paulo", "valor_gasto_total": 29000.00},
    {"id": 102, "nome": "Maria Oliveira", "idade": 38, "sexo": "Feminino", "cidade": "Rio de Janeiro", "valor_gasto_total": 30800.00},
    {"id": 103, "nome": "Carlos Souza", "idade": 50, "sexo": "Masculino", "cidade": "Belo Horizonte", "valor_gasto_total": 30000.00},
    {"id": 104, "nome": "Ana Santos", "idade": 55, "sexo": "Feminino", "cidade": "Porto Alegre", "valor_gasto_total": 7500.00},
    {"id": 105, "nome": "Pedro Costa", "idade": 42, "sexo": "Masculino", "cidade": "Brasília", "valor_gasto_total": 19300.00},
    {"id": 106, "nome": "Sofia Pereira", "idade": 48, "sexo": "Feminino", "cidade": "Recife", "valor_gasto_total": 15000.00},
    {"id": 107, "nome": "José Santos", "idade": 60, "sexo": "Masculino", "cidade": "Salvador", "valor_gasto_total": 2500.00},
    {"id": 108, "nome": "Paula Lima", "idade": 36, "sexo": "Feminino", "cidade": "Fortaleza", "valor_gasto_total": 38950.00},
    {"id": 109, "nome": "Luiz Oliveira", "idade": 47, "sexo": "Masculino", "cidade": "Manaus", "valor_gasto_total": 25000.00},
    {"id": 110, "nome": "Cristina Santos", "idade": 52, "sexo": "Feminino", "cidade": "Curitiba", "valor_gasto_total": 5000.00},
    {"id": 111, "nome": "Antonio Costa", "idade": 40, "sexo": "Masculino", "cidade": "Natal", "valor_gasto_total": 8300.00},
    {"id": 112, "nome": "Beatriz Silva", "idade": 43, "sexo": "Feminino", "cidade": "Florianópolis", "valor_gasto_total": 30000.00},
    {"id": 113, "nome": "Loja Propria", "idade": None, "sexo": None, "cidade": "Limeira", "valor_gasto_total": 39500.00},  # Adicionando valores para "idade" e "sexo"
]


dados_desempenho_produto = [
    {"produto": "Banheira", "vendas_totais": 26, "receita_total": 65000.00},
    {"produto": "Ofurô", "vendas_totais": 22, "receita_total": 37200.00},
    {"produto": "Spa", "vendas_totais": 21, "receita_total": 105000.00},  # Corrigindo a formatação dos dados
]
#estão sendo inicializados com os dados contidos nas variáveis
# Criando os DataFrames
df_vendas = pd.DataFrame(dados_vendas)
df_comportamento_cliente = pd.DataFrame(dados_comportamento_cliente)
df_desempenho_produto = pd.DataFrame(dados_desempenho_produto)
#O método .head() é usado para mostrar apenas as primeiras linhas de cada DataFrame
# Visualizando as primeiras linhas
print("DataFrame de Vendas:")
print(df_vendas.head())

print("\nDataFrame de Comportamento do Cliente:")
print(df_comportamento_cliente.head())

print("\nDataFrame de Desempenho do Produto:")
print(df_desempenho_produto.head())
