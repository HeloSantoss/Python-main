# Dados do desempenho do produto
desempenho_produto = [
    {"produto": "Banheira", "vendas_totais": 26, "receita_total": 65000.00},
    {"produto": "Ofurô", "vendas_totais": 22, "receita_total": 37200.00},
    {"produto": "Spa", "vendas_totais": 21, "receita_total": 105000.00}
]

# Calculando o preço médio por produto
for produto in desempenho_produto:
    preco_medio = produto["receita_total"] / produto["vendas_totais"]
    produto["preco_medio"] = preco_medio

# Exibindo o preço médio de cada produto
for produto in desempenho_produto:
    print(f"Produto: {produto['produto']}, Preço Médio: R${produto['preco_medio']:.2f}")
    