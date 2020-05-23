x = float(input("n1: "))
a = float(input("n2: "))
b = float(input("n3: "))
if (b <= a):
	print("Entradas ", a, " e ", b, " invalidas")
elif (a <= x) and (x <= b):
	print(x, "pertence ao intervalo", a,",", b )
else:
	print(x, "nao pertence ao intervalo", a,",", b)

