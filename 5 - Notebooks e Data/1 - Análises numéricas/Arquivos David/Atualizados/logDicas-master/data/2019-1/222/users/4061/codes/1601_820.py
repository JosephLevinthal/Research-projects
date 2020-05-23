# Instituto de Computacao - UFAM
# Lab 01 - Ex 10
# 20 / 05 / 2016

valor = int(input("Qual o valor do saque? "))

# Quantidade de notas de R$ 50
onca = valor // 50 

# Valor restante a ser sacado com notas menores que R$ 50
osso = valor % 50

# Quantidade de notas de R$ 10
bflor = osso // 10

# Valor restante a ser sacado com notas menores que R$ 50
necta = osso % 10

# Quantidade de notas de R$ 2
tartaruga = necta // 2

print(int(onca))
print(int(bflor))
print(int(tartaruga))
