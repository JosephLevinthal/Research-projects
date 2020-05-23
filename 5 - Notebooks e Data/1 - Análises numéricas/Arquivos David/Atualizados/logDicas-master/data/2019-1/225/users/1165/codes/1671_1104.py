a = float(input("Insira um valor: "))
b = float(input("Insira um valor: "))
c = float(input("Insira um valor: "))
d = float(input("Insira um valor: "))

if(b > a and d > c):
	if (c >= a and d <= a or c >= b and d <= b):
		print("Intervalo 1: ", a, ",", b)
		print("Intervalo 2: ", c, ",", d)
		print("Ha intersecao")
	elif (a >= c and a <= c or b >= d and b <= d):
		print("Intervalo 1: ", a, ",", b)
		print("Intervalo 2: ", c, ",", d)
		print("Ha intersecao")
	else:
		print("Intervalo 1: ", a, ",", b)
		print("Intervalo 2: ", c, ",", d)
		print("Nao ha intersecao")
else:
	print("Intervalo 1: ", a, ",", b)
	print("Intervalo 2: ", c, ",", d)
	print("Entradas invalidas")