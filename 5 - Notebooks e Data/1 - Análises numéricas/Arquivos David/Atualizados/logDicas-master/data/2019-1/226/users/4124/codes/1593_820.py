# Instituto de Computacao - UFAM
# Lab 01 - Ex 10
# 20 / 05 / 2016

valor = int(input("Qual o valor do saque? "))

# Quantidade de notas de R$ 50
not50 = valor // 50 

# Valor restante a ser sacado com notas menores que R$ 50
rest = valor % 50

# Quantidade de notas de R$ 10
not10 = rest // 10

# Valor restante a ser sacado com notas menores que R$ 50
rest10 = rest % 10

# Quantidade de notas de R$ 2
not2 = rest10 // 2

print(int(not50))
print(int(not10))
print(int(not2))
