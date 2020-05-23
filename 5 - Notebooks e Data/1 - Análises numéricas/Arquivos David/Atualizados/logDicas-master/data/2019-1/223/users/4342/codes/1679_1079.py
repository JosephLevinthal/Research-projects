from math import *
A = float(input ("Lado 1: "))
B = float(input ("Lado 2: "))
C = float(input ("Lado 3: "))

print("Entradas:",A,B,C)

# Testa se pelo menos uma das entradas eh negativa 
if ((A<0) or (B<0) or (C<0)):
	# Testa se medidas correspondem aas de um triangulo
	if (___COMPLETE AQUI___):
		s = (a + b + c) / 2.0
		area = sqrt(s * (s-A) * (s-B) * (s-C))
		area = round(area, 3)
		print("Area:", area)
	else:
		print("Area: invalida")
else:
	print("Area: invalida")
