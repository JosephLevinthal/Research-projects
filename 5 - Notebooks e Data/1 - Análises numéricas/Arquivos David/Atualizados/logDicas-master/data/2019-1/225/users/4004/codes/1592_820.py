# Instituto de Computacao - UFAM
# Lab 01 - Ex 10
# 20 / 05 / 2016

valor = float(input("Qual o valor do saque? "))

R50V = valor // 50 # Quantidade de notas de R$ 50

R50 = valor % 50 # Valor restante a ser sacado com notas menores que R$ 50

R10V = R50 // 10 # Quantidade de notas de R$ 10

R10 = R50 % 10 # Valor restante a ser sacado com notas menores que R$ 50

R2V = R10 // 2 # Quantidade de notas de R$ 2

print(int(R50V))
print(int(R10V))
print(int(R2V))
