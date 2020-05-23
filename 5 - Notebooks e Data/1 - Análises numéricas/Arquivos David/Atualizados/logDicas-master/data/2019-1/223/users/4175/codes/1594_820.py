# Instituto de Computacao - UFAM
# Lab 01 - Ex 10
# 20 / 05 / 2016

valor = int(input("Qual o valor do saque? "))

# Quantidade de notas de R$ 50
n50 = valor // 50

# Valor restante a ser sacado com notas menores que R$ 50
r50 = valor % 50

# Quantidade de notas de R$ 10
n10 = r50 // 10

# Valor restante a ser sacado com notas menores que R$ 50
r10 = r50 % 10

# Quantidade de notas de R$ 2
n2 = r10 // 2

print(int(n50))
print(int(n10))
print(int(n2))
