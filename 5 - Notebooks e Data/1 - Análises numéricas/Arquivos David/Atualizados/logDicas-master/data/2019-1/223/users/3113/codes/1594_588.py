# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.
# Instituto de Computacao - UFAM
# Lab 01 - Ex 10
# 20 / 05 / 2016

valor = int(input("Qual o valor do saque? "))

# Quantidade de notas de R$ 100
notas_RS100 = valor//100 
# Valor restante a ser sacado com notas menores que R$ 50
resto_RS100 = valor % 100

# Quantidade de notas de R$ 10
notas_RS50 = resto_RS100 // 50

# Valor restante a ser sacado com notas menores que R$ 50
resto_RS50 = resto_RS100 % 50

# Quantidade de notas de R$ 2
notas_RS10 = resto_RS50 // 10

print(int(notas_RS100))
print(int(notas_RS50))
print(int(notas_RS10))