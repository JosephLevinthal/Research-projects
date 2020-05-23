x = float(input())
a = float(input())
b = float(input())

if (b>a):
	if (a<= x <= b):
		print(x, "pertence ao intervalo", a, ",", b) 
	else:
		print(x, "nao pertence ao intervalo", a, ",", b)
else:
	print("Entradas", a,"e", b, "invalidas")