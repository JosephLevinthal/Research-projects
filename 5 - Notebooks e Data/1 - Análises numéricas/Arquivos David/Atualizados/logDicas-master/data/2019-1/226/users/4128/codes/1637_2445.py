e = input("escala (c/f): ")
t = float(input("temperatura: "))
if (e.lower() == "c"):
	f = (9 *t)/5 +32
	print(round(f, 2))
else:
	c = 5/9*(t - 32)
	print(round(c, 2))