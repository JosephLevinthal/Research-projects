# Ao testar sua solução, não se limite ao caso de exemplo.

from math import *

# Leitura dos lados do triangulo a, b, and c
A = float(input (" "))
B = float(input (" "))
C = float(input (" "))

print("Entradas:", A, ",", B, ",", C)

# Testa se pelo menos uma das entradas eh negativa 
if ( (A > 0) or (B > 0) or (C > 0) ):
	if( (A > 0) or (B > 0) or (C > 0) ):
	# Testa se medidas correspondem as de um triangulo
	if ( (A < B + C) and (B < A + C) and ( C < A + B) ) :
		s = (A + B + C) / 2.0
		area = sqrt( (s) * ((s-A) * (s-B) * (s-C)))
		area = round(area, 3)
		print("Area:", area)
	else:
		print("Area: invalida")
else:
	print("Area: invalida")
