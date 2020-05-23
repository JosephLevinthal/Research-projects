a = float(input("N1 "))
b = float(input("N2 "))
c = float(input("N3 "))
d = float(input("N4 "))
print("Intervalo 1:", a, ",", b)
print("Intervalo 2:", c, ",", d)

if(b>a and d>c):
	if((a<=c and b>=c) or (c<=a and b<=c) or (d>=a and b>=d) or (d<=a and d>=b)):
		print("Ha intersecao")
	else:
		print("Nao ha intersecao")
else:
	print("Entradas invalidas")