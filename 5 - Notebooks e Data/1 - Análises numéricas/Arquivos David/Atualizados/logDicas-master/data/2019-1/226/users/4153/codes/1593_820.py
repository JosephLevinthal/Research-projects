# Instituto de Computacao - UFAM
# Lab 01 - Ex 10
# 20 / 05 / 2016

valor = int(input("Qual o valor do saque? "))

# Quantidade de notas de R$ 50
notas_R50 = valor // 50

# Valor restante a ser sacado com notas menores que R$ 50
resto_R50 = valor % 50

# Quantidade de notas de R$ 10
notas_R10 = resto_R50 // 10

# Valor restante a ser sacado com notas menores que R$ 50
resto_R10 = resto_R50 % 10

# Quantidade de notas de R$ 2
notas_R2 = resto_R10 // 2

print(int(notas_R50))
print(int(notas_R10))
print(int(notas_R2))
