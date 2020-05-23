# Entradas
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
# Saidas pt.1
print("Intervalo 1: ", a, ",", b)
print("Intervalo 2: ", c, ",", d)
# Condicoes
if (b > a) and (d > c):
	if (a >= c) and (a <= d) or (b >= c) and (b <= d):
		print("Ha intersecao")
	elif (c >= a) and (c <= b) or (d >= a) and (d <= b):
		print("Ha intersecao")
	else: 
		print("Nao ha intersecao")
else:
	print("Entradas invalidas")
