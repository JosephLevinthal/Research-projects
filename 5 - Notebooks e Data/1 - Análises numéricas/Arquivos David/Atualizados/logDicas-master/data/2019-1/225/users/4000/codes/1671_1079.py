# Ao testar sua solução, não se limite ao caso de exemplo.

from math import *

# Leitura dos lados do triangulo a, b, and c
a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))

print("Entradas:", a, ",", b, ",", c)

# Testa se pelo menos uma das entradas eh negativa 
if (abs(b-c)<a<(b+c)):
	# Testa se medidas correspondem aas de um triangulo
   if (a+b > c):
	   s = (a + b + c) / 2.0
	   area = sqrt(s * (s-a) * (s-b) * (s-c))
	   A = round(area, 3)
	   print("Area:", A)
else:
	print("Area: invalida")

