import matplotlib.pyplot as plt

# Dados dos clientes
comportamento_do_cliente = [
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
    {"id": 113, "nome": "Loja Propria", "sexo": "", "cidade": "Limeira", "valor_gasto_total": 39500.00}
]

# Coletar os valores gastos por cliente
valores_gastos = [cliente["valor_gasto_total"] for cliente in comportamento_do_cliente]

# Plotar o histograma
plt.figure(figsize=(10, 8))
plt.hist(valores_gastos, bins=10, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Distribuição dos Gastos dos Clientes')
plt.xlabel('Valor Gasto (R$)')
plt.ylabel('Número de Clientes')
plt.grid(True)
plt.show()
