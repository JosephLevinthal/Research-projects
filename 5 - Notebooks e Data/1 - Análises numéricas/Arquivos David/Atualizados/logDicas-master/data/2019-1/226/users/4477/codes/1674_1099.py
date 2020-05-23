a = float(input("lado x: "))
b = float(input("lado y: "))
c = float(input("lado z: "))

print ("Entradas:", a, ",", b, ",", c )

if (a < c + b and b < a + c and c < b + a):
	if (a == b and b == c):
		print("Tipo de triangulo: equilatero")
	elif (a == b and b != c or b == c and b != a):
		print("Tipo de triangulo: isosceles")
	else:
		print("Tipo de triangulo: escaleno")
else:
	print("Tipo de triangulo: invalido")