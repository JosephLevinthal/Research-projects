a = float(input("valor: "))
b = float(input("valor: "))
c = float(input("valor: "))
d = float(input("valor: "))
e = float(input("valor: "))
f = float(input("valor: "))

p = (a * e) - (b * d) 

if(p != 0):
	x = ((c * e) - (b * f)) / ((a * e) - (b * d))
	y = ((a * f) - (c * d)) / ((a * e) - (b * d))
	print(x)
	print(y)
else:
	print("Nao tem solucao")
	



