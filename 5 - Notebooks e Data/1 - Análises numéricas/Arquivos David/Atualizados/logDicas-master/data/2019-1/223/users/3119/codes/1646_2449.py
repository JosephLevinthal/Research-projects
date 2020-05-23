a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))
d = float(input("Valor de d: "))
e = float(input("Valor de e: "))
f = float(input("Valor de f: "))

valor = (a*e) - (b*d)

if(valor != 0):
	x = ((c*e) - (b*f))/ valor
	print(x)
	y = ((a*f) - (c*d)) / valor
	print(y)
else:
	print("Nao tem solucao")


	