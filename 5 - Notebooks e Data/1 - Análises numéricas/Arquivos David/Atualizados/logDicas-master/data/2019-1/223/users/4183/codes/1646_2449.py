a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))
d = float(input("Valor de d: "))
e = float(input("Valor de e: "))
f = float(input("Valor de f: "))

if (a*e - b*d == 0):
	print("Nao tem solucao")
else: 
	x = (c*e - b*f)/(a*e - b*d)
	y = (a*f - c*d)/(a*e - b*d)
	print(x)
	print(y)
	
	