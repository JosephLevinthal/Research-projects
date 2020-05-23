a=float(input("valor de a: "))
b=float(input("valor de b: "))
c=float(input("valor de c: "))
d=float(input("valor de d: "))
print("Intervalo 1: ", a, ",", b)
print("Intervalo 2: ", c, ",", d)
if (b>a) and (d>c)and (a==c) or (a==d) or (b==c) or (b==d) or (b>c) or (d<b):
	print("Ha intersecao")
elif(b>a) and (d>c):
	print(" Nao ha intersecao")
else:
	print("Entradas invalidas")
	



