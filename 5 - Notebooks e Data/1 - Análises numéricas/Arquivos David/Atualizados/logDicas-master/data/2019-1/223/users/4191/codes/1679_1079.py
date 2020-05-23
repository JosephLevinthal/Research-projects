# Ao testar sua solução, não se limite ao caso de exemplo.

from math import *

# Leitura dos lados do triangulo a, b, and c
A = float(input("Lado 1: "))
B = float(input("Lado 2: "))
C = float(input("Lado 3: "))

print("Entradas:", A, ",", B, ",", C)

# Testa se pelo menos uma das entradas eh negativa 
if ((A > 0) and (B > 0) and (C > 0)):
	# Testa se medidas correspondem aas de um triangulo
	if ((A+B > C) and (B+C > A) and (A+C > B)):
		s = (A + B + C) / 2.0
		area = sqrt(s * (s-A) * (s-B) * (s-C))
		area = round(area, 3)
		print("Area:", area)
	else:
		print("Area: invalida")
else:
	print("Area: invalida")
