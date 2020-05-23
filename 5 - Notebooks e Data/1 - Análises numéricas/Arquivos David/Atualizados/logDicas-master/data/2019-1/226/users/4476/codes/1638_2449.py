a = float(input("valor: "))
b = float(input("valor: "))
c = float(input("valor: "))
d = float(input("valor: "))
e = float(input("valor: "))
f = float(input("valor: "))

x = ((c*e)-(b*f)) / ((a*e)-(b*d))
y = ((a*f)-(c*d)) / ((a*e)-(b*d))

if (a, e, b, d != 0):
	print(float(x))
	print(y)
	
else:
	print("Nao tem solucao")
	
	