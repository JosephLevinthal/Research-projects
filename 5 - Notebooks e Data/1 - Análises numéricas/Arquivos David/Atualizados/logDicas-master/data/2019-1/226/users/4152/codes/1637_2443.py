# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *

r = float(input("Digite aqui o raio do tanque: "))

x = float(input("Digite aqui a altura na parte superior: "))

num = input("Digite aqui o numero da opcao desejada: ")

cal2 = (4 * pi * (r ** 3)) / 3

cal1 = ((pi * x ** 2) * (3 * r - x)) / 3

if (num == "1"):
	cal = cal1
else:
	cal = cal2 - cal1
	
print(round(cal, 4))