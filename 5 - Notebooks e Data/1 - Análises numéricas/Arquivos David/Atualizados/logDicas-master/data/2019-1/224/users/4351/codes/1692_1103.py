x=float(input("valor de x: "))
a=float(input("valor de a: "))
b=float(input("valor de b: "))
if (a<b) and (x<b) and (x>a):
	print(x, "pertence ao intervalo", a, ",", b)
elif(a<b) and (x>b):
	print(x," nao pertence ao intervalo", a, ",", b)
elif(a<b) and (x<a):
	print(x," nao pertence ao intervalo", a, ",", b)
else:
	print("Entradas", a, "e", b, "invalidas")