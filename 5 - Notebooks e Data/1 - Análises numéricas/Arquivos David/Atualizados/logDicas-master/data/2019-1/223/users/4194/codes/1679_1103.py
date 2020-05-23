x = float(input("x: "))
a = float(input("a: "))
b = float(input("b: "))

if(b <= a):
	print("Entradas", a, "e", b, "invalidas")
elif(a <= x <= b):
	print(x, "pertence ao intervalo", a, ",", b)
else:
	print(x, "nao pertence ao intervalo", a, ",", b)