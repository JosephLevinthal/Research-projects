a = float(input("medidaa: "))
b = float(input("medidab: "))
c = float(input("medidac: "))
print("Entradas:", a, ",", b, ",", c)
if((a != 0) and (b != 0) and (c != 0)):
	if((a < b + c) and (b < a + c) and (c < b + a)):
	
		if((a != b) and (b != c) and (c != a)):
			print("Tipo de triangulo: escaleno")
		else:
			if((a == b) or (b == c)):
				print("Tipo de triangulo: isosceles")  
			else:
				print("Tipo de triangulo: equilatero")
	else:
		print("Tipo de triangulo: invalido")
else:
	print("Tipo de triangulo: invalido")