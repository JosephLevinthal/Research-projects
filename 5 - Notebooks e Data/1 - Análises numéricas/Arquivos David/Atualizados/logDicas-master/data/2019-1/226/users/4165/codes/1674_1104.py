a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))
d = float(input("Entre com o valor de d: "))

print("Intervalo 1:", a, ",", b)
print("Intervalo 2:", c, ",", d)

if(b > a) and (d > c):
	if c>=a and c<=b:
		print("Ha intersecao")
	else:
		print("Nao ha intersecao")
else:
	print("Entradas invalidas")