a = float(input("valor de a: "))
b = float(input("valor de b: "))
c = float(input("valor de c: "))
d = float(input("valor de d: "))

print("Intervalo 1:", a, ",", b)
print("Intervalo 2:", c, ",", d)

if((b <= a) or (d <= c)):
	print("Entradas invalidas")
elif(b < c):
		print("Nao ha intersecao")
else:
	print("Ha intersecao")