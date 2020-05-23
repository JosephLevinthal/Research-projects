# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
r = float(input("digite o raio: "))
x = float(input("digite a altura: "))
y = int(input("digite um numero em um intervalo de 1 ate 2: "))

Vt = (4*pi*(r**3))/3
Vx = round((pi*(x**2)*((3*r) - x))/3,4)

vC = round(Vt - Vx,4)

if y == 1:
	print(Vx)
else:
	print(vC)
