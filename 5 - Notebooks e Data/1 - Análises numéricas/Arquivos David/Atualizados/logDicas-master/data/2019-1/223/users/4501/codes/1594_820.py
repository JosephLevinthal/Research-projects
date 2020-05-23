# Instituto de Computacao - UFAM
# Lab 01 - Ex 10
# 20 / 05 / 2016

valor = int(input("Qual o valor do saque? "))

# Quantidade de notas de R$ 50
Notas50 = valor // 50 

# Valor restante a ser sacado com notas menores que R$ 50
Resto50 = valor % 50

# Quantidade de notas de R$ 10
Notas10 = Resto50 // 10

# Valor restante a ser sacado com notas menores que R$ 50
Resto10 = Resto50 % 10

# Quantidade de notas de R$ 2
Notas2 = Resto10 // 2

print(Notas50)
print(Notas10)
print(Notas2)
