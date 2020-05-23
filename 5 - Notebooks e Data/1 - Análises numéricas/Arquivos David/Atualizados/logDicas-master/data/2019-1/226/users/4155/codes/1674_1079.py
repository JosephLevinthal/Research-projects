from math import *

A = float(input("Lado 1: "))
B = float(input("Lado 2: "))
C = float(input("Lado 3: "))

print("Entradas:", A, ",", B, ",", C)
 
if ((A >= 0) and (B >= 0) and (C >= 0)):
	if((A < B + C) and (B < C + A) and (C < A + B)):
		s = (A + B + C) / 2.0
		area = sqrt(s * (s - A) * (s - B) * (s - C))
		r = round(area, 3)
		print("Area:", r)
	else:
		print("Area: invalida")
else:
	print("Area: invalida")
