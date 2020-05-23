a= float(input("escolha um valor para a: "))
b= float(input("escolha um valor para b: "))
c= float(input("escolha um valor para c: "))
d= float(input("escolha um valor para d: "))
if (b>a) and (d>c) and (a==c) or (a==d) or (b==c) or (b==d) or (b>c) or (d<b):
	print("Intervalo 1:", a, ",", b)
	print("Intervalo 2:", c, ",", d)
	print("Ha intersecao")
elif (b>a) and (d>c):
	print("Intervalo 1:", a, ",", b)
	print("Intervalo 2:", c, ",", d)
	print("Nao ha intersecao")
else:
	print("Intervalo 1:", a, ",", b)
	print("Intervalo 2:", c, ",", d)
	print("Entradas invalidas")