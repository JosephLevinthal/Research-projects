a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
print("Intervalo 1:", a,",", b)
print("Intervalo 2:", c,",", d)
if b>=a and d>=c:
	if (c>=a and c<=b) or (d>=a and d<=b):
		print("Ha intersecao")
	else:
		print("Nao ha intersecao")
else:
	print("Entradas invalidas")