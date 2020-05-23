# Ao testar sua solução, não se limite ao caso de exemplo.

from math import *

# Leitura dos lados do triangulo a, b, and c
a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))

print("Entradas:", a, ",", b, ",", c)


if (c+b>a and a+c>b and b+a>c):
	if(a==b==c):
		print("Tipo de triangulo: equilatero")
	else:
		if(a==b and b!=c) or (b==c and c!=a):
			print("Tipo de triangulo: isosceles")
		else:
			print("Tipo de triangulo: escaleno")
else:
			print("Tipo de triangulo: invalido")