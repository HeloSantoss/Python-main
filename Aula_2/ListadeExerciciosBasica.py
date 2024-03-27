# Lista de Exercícios sobre Operadores e Tipos de Variáveis em Python

# 1-
a = 10
b = 2
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisaoInt = a // b
restoDivisao = a % b
potenciacao = a ** b

# Calculando área de um círculo
import math

pi = math.pi
raio = 2
area_circulo = pi * raio ** 2
print("Área do círculo:", area_circulo)

# 2
nome = "Heloisa"
sobrenome = "Santos"
nome_completo = nome + " " + sobrenome

# Converter para letras maiúsculas
nome_completo_upper = nome_completo.upper()

# Substituir parte do texto
nome_completo_substituido = nome_completo.replace("Heloisa", "Graziele")

# 3
# Listas (mutáveis)
frutas = ["azul", "branco", "verde"]
numeros = [1, 2, 3, 4, 5]

# Adicionando elementos a uma lista
frutas.extend(["laranja", "roxo"])
print(frutas)

# Tuplas (imutáveis)
coordenadas = (4, 5)
cores_rgb = (255, 0, 0)

# 4

# Variáveis booleanas
tem_sol = False
tem_chuva = False

# Expressões booleanas
if tem_sol and not tem_chuva
else
 "É um dia agradavel!"
dia_agradavel = tem_sol and not tem_chuva
dia_desagradavel = tem_chuva or not tem_sol
print("Dia agradável?", dia_agradavel)
print("Dia desagradável?", dia_desagradavel)
