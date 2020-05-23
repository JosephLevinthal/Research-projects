# Instituto de Computacao - UFAM
# Lab 01 - Ex 10
# 20 / 05 / 2016

valor = int(input("Qual o valor do saque? "))

# Quantidade de notas de R$ 50
cinquenta = int(valor / 100)

# Valor restante a ser sacado com notas menores que R$ 50
cinquenta = valor % 50

# Quantidade de notas de R$ 10
dez = cinquenta / 10

# Valor restante a ser sacado com notas menores que R$ 50
dez= dez % 10

# Quantidade de notas de R$ 2
dois = dez// 2

print(int(cinquenta))
print(int(dez))
print(int(dois))
