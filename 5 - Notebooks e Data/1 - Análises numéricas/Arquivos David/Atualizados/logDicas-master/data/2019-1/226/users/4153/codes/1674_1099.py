a = float(input("Insira o lado: "))
b = float(input("Insira o lado: "))
c = float(input("Insira o lado: "))

print("Entradas:",a, ",",b, ",",c)

if((a >= b + c) or (b>= a + c) or (c >= b + a)):
	print("Tipo de triangulo: invalido")
elif((a == b) and ( b == c)):
	print("Tipo de triangulo: equilatero")
elif((a == b) or (b == c) or (c == a)):
	print("Tipo de triangulo: isosceles")
elif((a != b) and (b != c)):
	print("Tipo de triangulo: escaleno")