# Ao testar sua solução, não se limite ao caso de exemplo.

from math import *

# Leitura dos lados do triangulo a, b, and c
a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))

print("Entradas:", a, ",", b, ",", c)

# Testa se pelo menos uma das entradas eh negativa 
if (a > 0  and b > 0 and c > 0):
	
	# Testa se medidas correspondem aas de um triangulo
	if (a + b > c and a + c > c and c + b > a): #And, todas precisam ser verdadeiras ao mesmo tempo.
		s = (a + b + c) / 2.0
		area = sqrt(s * (s-a) * (s-b) * (s-c))
		print("Area:" ,round(area, 3)) #acredito que a esssa altura o round ta aí tranquilão
	else:
		print("Area: invalida")
else:
	print("Area: invalida")
#lembrar que o if casa com seu respectivo else , no caso o primeiro if "pareia" com o ultimo else
#pois se um numero de entrada for negativo automaticamente cai no else sem passar pelo segundo if
#e só.