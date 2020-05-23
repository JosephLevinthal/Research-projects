x = float(input("x: "))
a = float(input("a: "))
b = float(input("b: "))
if b > a:
	if a<=x and x<=b:
		print(x, "pertence ao intervalo", a,",",b)
	else:
		print(x, "nao pertence ao intervalo", a,",",b)
else:
	print("Entradas",a,"e",b,"invalidas")
