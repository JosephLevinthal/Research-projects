# Instituto de Computacao - UFAM
# Lab 01 - Ex 10
# 20 / 05 / 2016

valor = int(input("Qual o valor do saque? "))

# Quantidade de notas de R$ 50
notas_50 = valor // 50 

# Valor restante a ser sacado com notas menores que R$ 50
resto_50 = valor % 50

# Quantidade de notas de R$ 10
notas_10 = resto_50 // 10

# Valor restante a ser sacado com notas menores que R$ 50
resto_10 = resto_50 % 10

# Quantidade de notas de R$ 2
notas_2 = resto_10 // 2

print(int(notas_50))
print(int(notas_10))
print(int(notas_2))
