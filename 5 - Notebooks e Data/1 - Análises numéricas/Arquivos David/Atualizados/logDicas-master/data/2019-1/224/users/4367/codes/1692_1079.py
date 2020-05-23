# Ao testar sua solução, não se limite ao caso de exemplo.

from math import *

# Leitura dos lados do triangulo a, b, and c
a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))
d=max(a,b,c)
e=min(a,b,c)
f=a+b+c-(d+e)

print("Entradas:", a, ",", b, ",", c)

# Testa se pelo menos uma das entradas eh negativa 
if not(a<0) or not(b<0) or not(c<0):
	# Testa se medidas correspondem as de um triangulo
	if e+f>d:
		s = (a + b + c) / 2.0
		area = sqrt(s * (s-a) * (s-b) * (s-c))
		area = round(area, 3)
		print("Area:", area)
	else:
		print("Area: invalida")
else:
	print("Area: invalida")
