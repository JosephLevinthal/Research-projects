a = float(input("digite a:"))
b = float(input("digite b:"))
c = float(input("digite c:"))
d = float(input("digite b:"))

print("Intervalo 1:", a, ",", b)
print("Intervalo 2:", c, ",", d)

if (b>a and d>c):
	if (a >= c and a <= d):
		print("Ha intersecao")
	elif (b >= c and b <= d):
		print("Ha intersecao")
	elif (c >= a and c <= b):
		print("Ha intersecao")
	elif (d >= a and d <= b):
		print("ha intersecao")
	else:
		print("Nao ha intersecao")
else:
	print("Entradas invalidas")
