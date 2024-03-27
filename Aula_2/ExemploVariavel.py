#Operações com Variáveis:
#_salario

salario = 3000
bonus = 500
salario_total = salario + bonus

print(salario_total)

#Manipulação de Strings:

nome = "Maria"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome

print(nome_completo)

#Atualização de Variáveis:

contador = 0
contador += 1
print(contador)

#Variáveis em Estruturas de Controle:
#sempre após o if devo colocar dois pontos, e dar espaço naproxima linha

idade = 18
if idade >= 18:
    pode_votar = True
else:
    pode_votar = False
    
    
#Por exemplo, se você tentar somar uma string com um número, Python gerará um erro:

numero = "42"
texto = "Python"

resultado = numero + texto  #Isso resultará em um TypeError
print(f"{numero}" + texto)

resultado = numero + texto
print(resultado)



