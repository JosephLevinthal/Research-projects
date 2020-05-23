from math import*
a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))

print("Entradas:", a, ",", b, ",", c)

if (a>0 and b>0 and c>0):
	
	if (a+c > b):
		s = (a + b + c) / 2.0
		area = sqrt(s*(s-a)*(s-b)*(s-c))
		A = round(area, 3)
		print("Area:" , A)
	
else:
print("Area: invalida")