n1 = float(input("Digite n1:"))
n2 = float(input("Digite n2: "))
n3 = float(input("Digite n3: "))

print("Entradas:", n1, ",", n2, ",", n3)

if ((n1 >= n2 + n3) or (n2>= n1 + n3) or (n3>= n2 + n1)):
	print ("Tipo de triangulo: invalido")
else:
	if((n1==n2) and (n2==n3)):
		print("Tipo de triangulo: equilatero")
	else:
		if((n1 == n2) or (n2 == n3) or (n3 == n1)):
			print ("Tipo de triangulo: isosceles")
		else:
			print("Tipo de triangulo: escaleno")