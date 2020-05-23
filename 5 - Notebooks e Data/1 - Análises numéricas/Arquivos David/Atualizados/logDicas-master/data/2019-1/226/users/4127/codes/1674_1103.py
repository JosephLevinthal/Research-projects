x = float(input("valor de x: "))
a = float(input("valor de a: "))
b = float(input("valor de b: "))
if (b<=a):
	print("Entradas", a, "e", b, "invalidas")
elif (a<=x<=b):
	print(x, "pertence ao intervalo", a,",", b)
else:
	print(x, "nao pertence ao intervalo", a,",", b)