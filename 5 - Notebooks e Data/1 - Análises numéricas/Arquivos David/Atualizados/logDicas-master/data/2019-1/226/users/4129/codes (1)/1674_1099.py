from math import*
a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))

print("Entradas:", a, ",", b, ",", c)

if(a < 0 or b < 0 or c < 0):
	print("Tipo de triangulo: invalido")
elif(a + b > c  and c + b > a  and a + c > b):
	if(a == b and b == c):
		print("Tipo de triangulo: equilatero")
	elif ((a==b or b==c) and (a!=b or b!=c)):
		print("Tipo de triangulo: isosceles")
	else:
		print("Tipo de triangulo: escaleno")
	
else:
	print("Tipo de triangulo: invalido")