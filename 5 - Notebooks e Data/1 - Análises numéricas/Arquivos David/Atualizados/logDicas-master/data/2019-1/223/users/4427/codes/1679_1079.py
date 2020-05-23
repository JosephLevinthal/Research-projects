# Ao testar sua solução, não se limite ao caso de exemplo.

from math import *

# Leitura dos lados do triangulo a, b, and c
a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))

print("Entradas:", a, ",", b, ",", c)

# Testa se pelo menos uma das entradas eh negativa 
if (a>0 and b>0 and c>0):
	# Testa se medidas correspondem as de um triangulo
	if ((a >= b + c) or (b >= c + a) or (c >= a + b)):
		print("Area: invalida")
	else:
		s = (a + b + c) / 2.0
		area = sqrt(s * (s-a) * (s-b) * (s-c))
		area = round(area, 3)
		print("Area:", area)
		
else:
	print("Area: invalida")
