x = float(input("Valor x:"))
a = float(input("Valor a:"))
b = float(input("Valor b:"))

if (b <= a):
	print("Entradas",a,"e",b,"invalidas")
elif (a <= x and x <= b):
	print(x,"pertence ao intervalo",a,",",b)
else:
	print(x,"nao pertence ao intervalo",a,",", b)

