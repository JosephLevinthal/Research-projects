x = float(input("Lado x: "))
y = float(input("Lado y: "))
z = float(input("Lado z: "))

print("Entradas:", x, ",", y, ",", z)

if((x < y + z) and(y < x + z) and(z < y + x)):
	if(x==y)and(y==z)and(z==x):
		print("Tipo de triangulo: equilatero")
	elif((x == y) or(y == z)):
		print("Tipo de triangulo: isosceles")  
	elif(x != y) and(y != z) and(z != x):
		print("Tipo de triangulo: escaleno")
	else:
		print("Tipo de triangulo: invalido")
else:
	print("Tipo de triangulo: invalido")