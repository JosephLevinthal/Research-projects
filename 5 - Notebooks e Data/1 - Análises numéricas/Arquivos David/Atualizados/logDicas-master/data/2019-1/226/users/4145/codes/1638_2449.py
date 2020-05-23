a = float(input("valor de a: "))
b = float(input("valor de b: "))
c = float(input("valor de c: "))
d = float(input("valor de d: "))
e = float(input("valor de e: "))
f = float(input("valor de f: "))


if(a*e-b*d == 0):
	
	print(" Nao tem solucao")
	
else:
	x = (c*e - b*f)/(a*e - b*d)
	y = (a*f - c*d)/(a*e - b*d)
	print(x)
	print(y)
