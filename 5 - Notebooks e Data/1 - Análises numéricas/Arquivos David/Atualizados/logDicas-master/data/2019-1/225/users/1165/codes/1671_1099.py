a = float(input("valor de a: "))
b = float(input("valor de b: "))
c = float(input("valor de c: "))

print ("Entradas: ",a, ",", b, ",",c ) 
if ((a > b+c) or (b > a+c) or (c > a+b)):
	msg = "invalido"
else:
	if ((a == b) and (b == c)):
		msg = "equilatero"
	else:
		if ((a == b) or (b == c) or (c == a)):
			msg = "isosceles"
		else:
			msg = "escaleno"

print("Tipo de triangulo: " + msg)

