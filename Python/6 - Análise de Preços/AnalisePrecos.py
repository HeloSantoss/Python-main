import matplotlib.pyplot as plt
import numpy as np

# Dados das vendas
vendas = [
    {"id": 1, "data": '2023-01-05', "produto": "Banheira", "quantidade": 2, "preco_unitario": 2500.00, "cliente_id": 101},
    {"id": 2, "data": '2023-02-12', "produto": "Ofurô", "quantidade": 1, "preco_unitario": 3000.00, "cliente_id": 113},
    {"id": 3, "data": '2023-03-20', "produto": "Spa", "quantidade": 3, "preco_unitario": 5000.00, "cliente_id": 103},
    {"id": 4, "data": '2023-04-10', "produto": "Banheira", "quantidade": 1, "preco_unitario": 2500.00, "cliente_id": 104},
    {"id": 5, "data": '2023-05-15', "produto": "Ofurô", "quantidade": 2, "preco_unitario": 3000.00, "cliente_id": 105},
    {"id": 6, "data": '2023-06-25', "produto": "Spa", "quantidade": 2, "preco_unitario": 5000.00, "cliente_id": 106},
    {"id": 7, "data": '2023-07-05', "produto": "Banheira", "quantidade": 1, "preco_unitario": 2500.00, "cliente_id": 113},
    {"id": 8, "data": '2023-08-18', "produto": "Ofurô", "quantidade": 3, "preco_unitario": 3000.00, "cliente_id": 108},
    {"id": 9, "data": '2023-09-30', "produto": "Spa", "quantidade": 1, "preco_unitario": 5000.00, "cliente_id": 109},
    {"id": 10, "data": '2023-10-08', "produto": "Banheira", "quantidade": 2, "preco_unitario": 2500.00, "cliente_id": 110},
    {"id": 11, "data": '2023-11-12', "produto": "Ofurô", "quantidade": 1, "preco_unitario": 3000.00, "cliente_id": 111},
    {"id": 12, "data": '2023-12-20', "produto": "Spa", "quantidade": 3, "preco_unitario": 5000.00, "cliente_id": 112},
    {"id": 13, "data": '2023-01-05', "produto": "Banheira", "quantidade": 3, "preco_unitario": 2500.00, "cliente_id": 101},
    {"id": 14, "data": '2023-02-12', "produto": "Ofurô", "quantidade": 1, "preco_unitario": 3000.00, "cliente_id": 102},
    {"id": 15, "data": '2023-03-20', "produto": "Spa", "quantidade": 2, "preco_unitario": 5000.00, "cliente_id": 103},
    {"id": 16, "data": '2023-04-10', "produto": "Banheira", "quantidade": 2, "preco_unitario": 2500.00, "cliente_id": 104},
    {"id": 17, "data": '2023-05-15', "produto": "Ofurô", "quantidade": 3, "preco_unitario": 3000.00, "cliente_id": 105},
    {"id": 18, "data": '2023-06-25', "produto": "Spa", "quantidade": 1, "preco_unitario": 5000.00, "cliente_id": 106},
    {"id": 19, "data": '2023-07-05', "produto": "Banheira", "quantidade": 1, "preco_unitario": 2500.00, "cliente_id": 107},
    {"id": 20, "data": '2023-08-18', "produto": "Ofurô", "quantidade": 2, "preco_unitario": 3000.00, "cliente_id": 108},
    {"id": 21, "data": '2023-09-30', "produto": "Spa", "quantidade": 3, "preco_unitario": 5000.00, "cliente_id": 109},
    {"id": 22, "data": '2023-10-08', "produto": "Banheira", "quantidade": 1, "preco_unitario": 2500.00, "cliente_id": 113},
    {"id": 23, "data": '2023-11-12', "produto": "Ofurô", "quantidade": 2, "preco_unitario": 3000.00, "cliente_id": 111},
    {"id": 24, "data": '2023-12-20', "produto": "Spa", "quantidade": 1, "preco_unitario": 5000.00, "cliente_id": 112},
    {"id": 25, "data": '2023-01-05', "produto": "Banheira", "quantidade": 2, "preco_unitario": 2500.00, "cliente_id": 113},
    {"id": 26, "data": '2023-02-12', "produto": "Ofurô", "quantidade": 3, "preco_unitario": 3000.00, "cliente_id": 102},
    {"id": 27, "data": '2023-03-20', "produto": "Spa", "quantidade": 1, "preco_unitario": 5000.00, "cliente_id": 103},
    {"id": 28, "data": '2023-04-10', "produto": "Banheira", "quantidade": 1, "preco_unitario": 2500.00, "cliente_id": 113},
    {"id": 29, "data": '2023-05-15', "produto": "Ofurô", "quantidade": 2, "preco_unitario": 3000.00, "cliente_id": 105}
]

# Agrupar os preços por produto
produtos = {}
for venda in vendas:
    produto = venda["produto"]
    preco_total = venda["quantidade"] * venda["preco_unitario"]
    if produto not in produtos:
        produtos[produto] = []
    produtos[produto].append(preco_total)

# Coletar os dados de preços
labels = []
precoss = []
for produto, preco in produtos.items():
    labels.append(produto)
    precoss.append(preco)

# Plotar o gráfico de caixa
plt.figure(figsize=(10, 6))
plt.boxplot(precoss, labels=labels, patch_artist=True)
plt.title('Distribuição de Preços dos Produtos')
plt.ylabel('Preço (R$)')
plt.xlabel('Produtos')
plt.grid(True)
plt.show()

