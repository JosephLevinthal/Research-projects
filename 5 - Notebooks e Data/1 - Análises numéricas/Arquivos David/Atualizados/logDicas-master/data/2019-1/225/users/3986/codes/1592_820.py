# Instituto de Computacao - UFAM
# Lab 01 - Ex 10
# 20 / 05 / 2016

VALOR = int(input("Qual o valor do saque? "))

# Quantidade de notas de R$ 50
qn50= VALOR // 50

# Valor restante a ser sacado com notas menores que R$ 50
r50 = VALOR % 50

# Quantidade de notas de R$ 10
qn10 = r50 // 10

# Valor restante a ser sacado com notas menores que R$ 50
re10 = r50 % 10

# Quantidade de notas de R$ 2
qn2 = re10 // 2

print(int(qn50))
print(int(qn10))
print(int(qn2))
