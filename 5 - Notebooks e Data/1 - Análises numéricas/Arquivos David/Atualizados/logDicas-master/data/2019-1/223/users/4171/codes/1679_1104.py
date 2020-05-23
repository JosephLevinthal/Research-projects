a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))

if (b > a) and (d > c):
	if (a <= c and c < b ) or (c <= b and b < d):
		print("Intervalo 1: ", a,",", b)
		print("Intervalo 2: ", c,",", d)
		print("Ha intersecao")
	elif (a > d) or (c > b):
		print("Intervalo 1: ", a,",", b)
		print("Intervalo 2: ", c,",", d)
		print("Nao ha intersecao")
elif (b <= a) or (d <= c):
		print("Intervalo 1: ", a,",", b)
		print("Intervalo 2: ", c,",", d)
		print("Entradas invalidas")

	