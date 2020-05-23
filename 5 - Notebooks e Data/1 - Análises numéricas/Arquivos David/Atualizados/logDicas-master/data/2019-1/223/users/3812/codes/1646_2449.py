a = float(input("digite o valor de a: "))
b = float(input("digite o valor de b: "))
c = float(input("digite o valor de c: "))
d = float(input("digite o valor de d: "))
e = float(input("digite o valor de e: "))
f = float(input("digite o valor de f: "))

if (a*e-b*d) != 0:

	x = (c*e-b*f)/(a*e-b*d) 
	y = (a*f-c*d)/(a*e-b*d)

	print(x)
	print(y)
else:

	print("Nao tem solucao")