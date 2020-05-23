a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
e = float(input("e: "))
f = float(input("f: "))
de = a * e - b * d
if (de != 0):
	x = (c * e - b * f) / de
	y = (a * f - c * d) / de
	print(x)
	print(y)
else:
	print("Nao tem solucao")
