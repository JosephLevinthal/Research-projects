x = float(input("Digite o valor do lado A: "))
y = float(input("Digite o valor do lado B: "))
z = float(input("Digite o valor do lado C: "))

print("Entradas: ", x, ",", y, ",", z)

if (x > 0) and (y > 0) and (z > 0):
	if (x < y+z) and (y < x+z) and (z < x+y):
		if (x == y) and (y == z):
			print("Tipo de triangulo: equilatero")
		elif (x != y) and (y != z):
			print("Tipo de triangulo: escaleno")
		else:
			print("Tipo de triangulo: isosceles")
	else:
		print("Tipo de triangulo: invalido")
else:
	print("Tipo de triangulo: invalido")
