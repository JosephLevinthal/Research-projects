a=float(input(","))
b=float(input(","))
c=float(input(","))
print("Entradas: ",a,",",b,",",c,",")

if ((a>=b+c)or(b>=a+c)or(c>=b+a)):
	print("Tipo de triangulo: invalido")
else:
	if ((a==b)and(b==c)):
		print("Tipo de triangulo: equilatero")
	else:
		if ((a==b)or(a==c)or(c==b)):
			print("Tipo de triangulo: isosceles")
		else:
			print("Tipo de triangulo: escaleno")