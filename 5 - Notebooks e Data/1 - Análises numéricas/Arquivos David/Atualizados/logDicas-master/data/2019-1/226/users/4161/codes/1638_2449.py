a = float(input("valor de a: "))
b = float(input("valor de b: "))
c = float(input("valor de c: "))
d = float(input("valor de d: "))
e = float(input("valor de e: "))
f = float(input("valor de f: "))
z1 = a*e - b*d
if (z1 == 0):
	print("Nao tem solucao")
else:
	x = (c*e - b*f)/z1
	y = (a*f - c*d)/z1
	print(x)
	print(y)