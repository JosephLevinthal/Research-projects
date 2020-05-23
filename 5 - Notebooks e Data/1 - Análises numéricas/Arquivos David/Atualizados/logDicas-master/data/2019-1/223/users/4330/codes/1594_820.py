# Instituto de Computacao - UFAM
# Lab 01 - Ex 10
# 20 / 05 / 2016

valor = input(" 138 ")

# Quantidade de notas de R$ 50
valor // 2 = notas_R$50

# Valor restante a ser sacado com notas menores que R$ 50
resto_R$50 = valor % 50

# Quantidade de notas de R$ 10
notas_R$10 = resto_R$50 // 10

# Valor restante a ser sacado com notas menores que R$ 50
resto_R$10 = resto_R$50 % 10

# Quantidade de notas de R$ 2
notas_R$2 = resto_R$10 // 2

print(int(notas_R$50))
print(int(notas_R$10))
print(int(notas_R$2))
