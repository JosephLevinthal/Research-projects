# Instituto de Computacao - UFAM
# Lab 01 - Ex 10
# 20 / 05 / 2016

valor=int(input("Qual o valor do saque? "))

# Quantidade de notas de R$ 50
var1=valor//50

# Valor restante a ser sacado com notas menores que R$ 50
var2=valor%50

# Quantidade de notas de R$ 10
var3=var2//10

# Valor restante a ser sacado com notas menores que R$ 50
var4=var2%10

# Quantidade de notas de R$ 2
var5=var4//2

print(int(var1))
print(int(var3))
print(int(var5))
