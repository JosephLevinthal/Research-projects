from math import *
	
a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))
	
print("Entradas:", a, ",", b, ",", c)	

if ((a >= b + c) or (b >= a + c) or (c >= a + b)):
	X = "invalido"
elif ((a != b) and (b != c) and (a != c)):
	X = "escaleno"
elif ((a != b) or (b != c) or (a != c)):
	X = "isosceles"
else:
	X = "equilatero"
					
print("Tipo de triangulo:", X)					
					