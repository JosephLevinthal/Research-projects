a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))
d = float(input("Valor de d: "))

print("Intervalo 1:", a, ",", b)
print("Intervalo 2:", c, ",", d)

if ((b <= a) or (d <= c)):
	print("Entradas invalidas")
elif (c < a) or (c > b):
	print("Nao ha intersecao")
else:
	print("Ha intersecao")
