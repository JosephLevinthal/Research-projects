a = float(input("Entrada a: "))
b = float(input("Entrada b: "))
c = float(input("Entrada c: "))
print("Entradas:", a, ",", b, ",", c)
if ((a >= b + c) or (b >= a + c) or (c >= a + b)):
	print("Tipo de triangulo: invalido")
else:
	if ((a == b) and (b == c)):
		print("Tipo de triangulo: equilatero")
	else:
		if ((a == b) or (b == c) or (a == c)):
			print("Tipo de triangulo: isosceles")
		else: 
			print("Tipo de triangulo: escaleno")