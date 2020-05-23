# Ao testar sua solução, não se limite ao caso de exemplo.

from math import *

# Leitura dos lados do triangulo a, b, and c
a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))

# Testa se pelo menos uma das entradas eh negativa 
if (a<0) or (b<0) or (c<0):
	print("Entradas:", a, ",", b, ",", c)
	print("Area: invalida")
else:
	if (a+b>c) and (a+c>b) and (b+c>a):
		s = (a + b + c) / 2.0
		area = sqrt(s * (s-a) * (s-b) * (s-c))
		area = round(area, 3)
		print("Entradas:", a, ",", b, ",", c)
		print("Area:", area)
	else:
		print("Entradas:", a, ",", b, ",", c)
		print("Area: invalida")

