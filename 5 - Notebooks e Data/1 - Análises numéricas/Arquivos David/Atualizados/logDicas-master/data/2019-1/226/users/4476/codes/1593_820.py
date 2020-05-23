# Instituto de Computacao - UFAM
# Lab 01 - Ex 10
# 20 / 05 / 2016

valor = int(input("Qual o valor do saque? "))

# Quantidade de notas de R$ 50
notas_Rs50 = valor // 50

# Valor restante a ser sacado com notas menores que R$ 50
resto_Rs50 = valor % 50

# Quantidade de notas de R$ 10
notas_Rs10 = resto_Rs50 // 10

# Valor restante a ser sacado com notas menores que R$ 50
resto_Rs10 = resto_Rs50 % 10

# Quantidade de notas de R$ 2
notas_Rs2 = resto_Rs10 // 2

print(int(notas_Rs50))
print(int(notas_Rs10))
print(int(notas_Rs2))
