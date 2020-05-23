# Ao testar sua solução, não se limite ao caso de exemplo.

from math import *

# Leitura dos lados do triangulo a, b, and c
a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))

print("Entradas:", a, ",", b, ",", c)

# Testa se pelo menos uma das entradas eh negativa 
if (a >= 0 and b >= 0 and c >= 0):
	# Testa se medidas correspondem aas de um triangulo
	if (min(a,b,c) + (a + b + c - max(a,b,c) - min(a,b,c)) > max(a,b,c)):
		s = (a + b + c) / 2.0
		area = sqrt(s * (s - a) * (s - b) * (s - c))
		x = round(area, 3)
		if x == 0:
			print("Area: invalida")
		else:
			print("Area: ", x)
	else:
		print("Area: invalida")
else:
	print("Area: invalida")