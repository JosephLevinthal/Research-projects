# Instituto de Computacao - UFAM
# Lab 01 - Ex 10
# 20 / 05 / 2016

a = int(input("Qual o valor do saque? "))

# Quantidade de notas de R$ 50
c = int(a//50)

# Valor restante a ser sacado com notas menores que R$ 50
d = a % 50

# Quantidade de notas de R$ 10
e = d // 10

# Valor restante a ser sacado com notas menores que R$ 50
f = d % 10

# Quantidade de notas de R$ 2
g = f // 2

print(int(c))
print(int(e))
print(int(g))
