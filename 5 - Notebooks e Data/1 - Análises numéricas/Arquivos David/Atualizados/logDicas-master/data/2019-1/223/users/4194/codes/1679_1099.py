a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))
print("Entradas: ", a, ",", b, ",", c)

if((a>=b+c) or (b>=a+c) or (c>=a+b)):
	print("Tipo de triangulo: invalido")
elif(a==b and b==c):
	print("Tipo de triangulo: equilatero")
elif((a == b) or (b==c) or (a==c)):
	print("Tipo de triangulo: isosceles")
elif(a!=b and b!=c and c!=a):
	print("Tipo de triangulo: escaleno")
else:
	print("Tipo de triangulo: invalido")