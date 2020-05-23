# Instituto de Computacao - UFAM
# Lab 01 - Ex 10
# 20 / 05 / 2016

valor = int(input("Qual o valor do saque? "))

# Quantidade de notas de R$ 50
notas_RS50 = valor//50 
# Valor restante a ser sacado com notas menores que R$ 50
resto_RS50 = valor % 50

# Quantidade de notas de R$ 10
notas_RS10 = resto_RS50 // 10

# Valor restante a ser sacado com notas menores que R$ 50
resto_RS10 = resto_RS50 % 10

# Quantidade de notas de R$ 2
notas_RS2 = resto_RS10 // 2

print(int(notas_RS50))
print(int(notas_RS10))
print(int(notas_RS2))
