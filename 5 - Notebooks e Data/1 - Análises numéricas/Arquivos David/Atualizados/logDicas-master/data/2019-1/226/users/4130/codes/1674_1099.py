a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

print("Entradas: ",a, ",",b, ", ",c)

x = "Tipo de triangulo: "

if ((a < 0) or (b < 0) or (c < 0) or (a >= b + c) or (b >= c + a) or (c >= a + b)):
	print(x, "invalido")
else:
	if(a == b) and (b == c):
		print(x, "equilatero")
	elif(a == b) or (b == c) or (c == a):
			print(x, "isosceles")
	else:
			print(x, "escaleno")