# Instituto de Computacao - UFAM
# Lab 01 - Ex 10
# 20 / 05 / 2016

VALOR =int(input("Qual o valor do saque?:"))

# Quantidade de notas de R$ 50
VALOR /50 

# Valor restante a ser sacado com notas menores que R$ 50
notas50= VALOR % 50

# Quantidade de notas de R$ 10
notas10 = resto// 10

# Valor restante a ser sacado com notas menores que R$ 50
resto10 = resto % 10

# Quantidade de notas de R$ 2
notas2 = resto10 // 2

print(int(notas))
print(int(notas10))
print(int(notas2))
