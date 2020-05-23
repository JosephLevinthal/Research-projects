x = float(input("Entre com o valor de x: "))
a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))

if (b > a):
	if (x>=a) and (x <=b):
		print(x, "pertence ao intervalo ", a, ",", b )
	else:
		print(x, "nao pertence ao intervalo ", a, ",", b)
else:
	print("Entradas", a, "e", b, " invalidas")