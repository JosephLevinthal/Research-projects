a = float(input(""))
b = float(input(""))
c = float(input(""))
d = float(input(""))
e = float(input(""))
f = float(input(""))

v = (a * e - b * d)
l = (a * e - b* d)
if (v == 0 and l == 0 ):
	print("Nao tem solucao")
else:
	x = (c * e - b * f) / (a * e - b * d)
	print(x)
	y = (a * f - c * d) / (a * e - b* d)
	print(y)