from math import *

# Leitura dos lados do triangulo a, b, and c
a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))

print("Entradas:", a, ",", b, ",", c)

# Verifica se algum lado é negativo
if a > 0 and b > 0 and c > 0:
	
	#testa medidas de um triangulo
	if (a + b > c and a + c > b and c + b > a):
		s = (a + b + c) / 2.0
		area = sqrt(s * (s-a) * (s-b) * (s-c))
		print("Area:", round(area, 3))
	else:
		print("Area: invalida")
else:
	print("Area: invalida")
