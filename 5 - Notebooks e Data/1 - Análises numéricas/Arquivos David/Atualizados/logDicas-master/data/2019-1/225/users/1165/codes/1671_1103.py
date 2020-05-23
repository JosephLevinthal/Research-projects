x = float(input("Leia numero real de x: "))
a = float(input("Leia o numero real de a: "))
b = float(input("Leia o numero real de b:"))

if ((a <= x and x <= b)):
	print(x , "pertence ao intervalo", a, ",", b)
elif (b <= a):
	print("Entradas", a, "e", b, "invalidas")
else:
	print(x , "nao pertence ao intervalo", a, ",", b)
	
