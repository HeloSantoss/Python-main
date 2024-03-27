import matplotlib.pyplot as plt

# Definindo os dados
desempenho_produto = [
    {"produto": "Banheira", "vendas_totais": 26, "receita_total": 65000.00},
    {"produto": "Ofurô", "vendas_totais": 22, "receita_total": 37200.00},
    {"produto": "Spa", "vendas_totais": 21, "receita_total": 105000.00}
]

# Calculando a receita total gerada por cada produto
#fornecem os valores dos dados para o gráfico
receita_por_produto = {produto['produto']: produto['receita_total'] for produto in desempenho_produto}

# Plotando o gráfico de pizza
#linha cria uma nova figura para o gráfico com uma largura de 8 polegadas e uma altura de 8 polegadas
plt.figure(figsize=(8, 8))
plt.pie(receita_por_produto.values(), labels=receita_por_produto.keys(), autopct='%1.1f%%', startangle=140)
#ndica o formato dos percentuais exibidos
plt.title('Distribuição da Receita por Produto')
plt.axis('equal')  # Garante que o gráfico de pizza seja desenhado como um círculo
plt.show()
