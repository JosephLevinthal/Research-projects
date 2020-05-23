x= float(input("Lado X:"))
y= float(input("Lado Y:"))
z= float(input("Lado Z:"))

print("Entradas:", x, ",", y, ",", z)

if ((x>= y+z) or (y>= x+z) or (z>= y+x)):
	print("Tipo de triangulo: invalido")

else: 
	if((x==y) and (y==z)):
		print("Tipo de triangulo: equilatero")
	else:
		if((x== y) or (y==z) or (z==x)):
			print("Tipo de triangulo: isosceles")
		else:
			print("Tipo de triangulo: escaleno")