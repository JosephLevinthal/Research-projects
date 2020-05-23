a = float(input("variavel a: "))
b = float(input("variavel b: "))
c = float(input("variavel c: "))
d = float(input("variavel d: "))
e = float(input("variavel e: "))
f = float(input("variavel f: "))

if (a * e) - (b * d) == 0:
	print("Nao tem solucao")
else:
	x = ((c * e) - (b * f)) / ((a * e) - (b * d))
	y = ((a * f) - (c * d)) / ((a * e) - (b * d))
	print(x)
	print(y)