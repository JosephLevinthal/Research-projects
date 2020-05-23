a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
print("Entradas:", a, ",", b, ",", c)
if (a < 0 or b < 0 or c < 0) or (a >= b + c or b >= a + c or c > a + b):
	print("Tipo de triangulo: invalido")
elif (a == b and b == c):
	print("Tipo de triangulo: equilatero")
elif (a == b or b == c or c == a):
	print("Tipo de triangulo: isosceles")
else:
	print("Tipo de triangulo: escaleno")

