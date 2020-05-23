# Ao testar sua s
from math import *
a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))
print("Entradas:", a, ",", b, ",", c) 
if((a>=b+c)or(b>=c+a)or(c>=b+a)):
	  print("Area: invalida")
else:
		s = (a + b + c) / 2.0
		area = sqrt(s * (s-a) * (s-b) * (s-c))
		area = round(area, 3)
		print("Area:", area)

