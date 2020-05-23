a = float(input("valor de a : "))
b = float(input("valor de b: "))
c = float(input("valor de c: "))
d = float(input("valor de d: "))
e = float(input("valor de e: "))
f = float(input("valor de f: "))

x = ((c*e) - (b*f))
x1 = ((a*e)-(b*d))
y = ((a*f) - (c*d))
y1 = ((a*e)-(b*d))

if (x1 == 0):
	(y1 == 0)
	print("Nao tem solucao ")
	
else:
	print(x/x1)
	print(y/y1)