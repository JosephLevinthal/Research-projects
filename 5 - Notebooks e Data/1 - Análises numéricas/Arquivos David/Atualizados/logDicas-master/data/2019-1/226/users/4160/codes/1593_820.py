# Instituto de Computacao - UFAM
# Lab 01 - Ex 10
# 25 / 03 / 2019

valor = int(input("Qual o valor do saque? "))

# Quantidade de notas de R$ 50
x = valor // 50 

# Valor restante a ser sacado com notas menores que R$ 50
y = valor % 50

# Quantidade de notas de R$ 10
b = y // 10
e = y % 10
# Valor restante a ser sacado com notas menores que R$ 50
d = y // 10 

# Quantidade de notas de R$ 2
a = e // 2

print(int(x))
print(int(d))
print(int(a))
