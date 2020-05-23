x = float(input("Valor de x: "))
a = float(input("Valor de a: "))
b = float(input("Valor de b: "))

if(b > a):
	if(a <= x <= b):
		print(x,"pertence ao intervalo", a,",", b )
	else:
		print(x,"nao pertence ao intervalo", a,",", b )
else:
	print("Entradas", a," e ",b ,"invalidas")