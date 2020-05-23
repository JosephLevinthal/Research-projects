from math import *
a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))

print("Entradas:", a, ",", b, ",", c)
if (abs(b - c)<a<(b + c)):
	if (a + b > c): 
		s = (a + b + c) / 2.0
		area = sqrt(s * (s-a) * (s-b) * (s-c))
		A = round(area, 3)
		print("Area:", A)
else:
	print("Area: invalida")

 