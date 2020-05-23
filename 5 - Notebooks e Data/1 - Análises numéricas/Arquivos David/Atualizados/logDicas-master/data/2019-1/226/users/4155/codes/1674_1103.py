x = float(input("valor de x: "))
a = float(input("valor de a: "))
b = float(input("valor de b: "))

if((b > a)):
	if((a <= x) and (x <= b)):
		print(x,"pertence ao intervalo", a,",", b)
	elif((a > x) or (x > b)):
		print(x,"nao pertence ao intervalo", a,",", b)
else:
	print("Entradas", a, "e", b, "invalidas")	
