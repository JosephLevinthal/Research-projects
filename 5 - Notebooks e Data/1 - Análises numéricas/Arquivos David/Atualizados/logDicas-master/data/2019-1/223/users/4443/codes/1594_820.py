# Instituto de Computacao - UFAM
# Lab 01 - Ex 10
# 28 / 03 / 2019

valor = int(input("Qual o valor do saque? "))

# Quantidade de notas de R$ 50
n50 = valor // 50

# Valor restante a ser sacado com notas menores que R$ 50
resto1 = valor % 50

# Quantidade de notas de R$ 10
n10 = resto1 // 10

# Valor restante a ser sacado com notas menores que R$ 50
resto2 = resto1 % 10

# Quantidade de notas de R$ 2
n2 = resto2 // 2

print(int(n50))
print(int(n10))
print(int(n2))
