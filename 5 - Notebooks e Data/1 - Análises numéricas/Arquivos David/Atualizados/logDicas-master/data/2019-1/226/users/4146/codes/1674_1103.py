x = float(input("Valor de x: "))
a = float(input("Valor de a: "))
b = float(input("Valor de b: "))

if (b <= a):
	print("Entradas", a, "e", b, "invalidas")
elif (a <= x <= b):
	print(x, "pertence ao intervalo", a, ",", b)
else:
	((x <= a) or (b <=x))
	print(x, "nao pertence ao intervalo", a, ",", b)