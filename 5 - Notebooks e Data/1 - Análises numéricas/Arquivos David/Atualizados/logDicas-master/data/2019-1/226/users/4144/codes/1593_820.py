# Instituto de Computacao - UFAM
# Lab 01 - Ex 10
# 20 / 05 / 2016

valor = (int(input("Qual o valor do saque? ")))

# Quantidade de notas de R$ 50
notas50 = valor // 50

# Valor restante a ser sacado com notas menores que R$ 50
rest50 = valor % 50

# Quantidade de notas de R$ 10
notas10 = rest50 // 10

# Valor restante a ser sacado com notas menores que R$ 50
rest10 = rest50 % 10

# Quantidade de notas de R$ 2
notas2 = rest10 // 2

print(int(notas50))
print(int(notas10))
print(int(notas2))
