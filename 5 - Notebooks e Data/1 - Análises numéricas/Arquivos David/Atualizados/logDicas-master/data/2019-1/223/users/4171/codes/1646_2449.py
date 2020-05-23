a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
e = float(input("e: "))
f = float(input("f: "))

g = (a * e -b * d)

if g == 0:
	print("Nao tem solucao")
else:
	x = (c * e - b * f) / g
	y = (a * f - c * d) / g
	print(x)
	print(y)