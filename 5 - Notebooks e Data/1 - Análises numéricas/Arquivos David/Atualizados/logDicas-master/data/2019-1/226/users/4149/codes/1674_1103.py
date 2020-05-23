x=float(input("valor x "))
a=float(input("valor a "))
b=float(input("valor b "))

if((b<=a)):
	print("Entradas",a,"e",b,"invalidas")
elif((a<=x<=b)):
	print(x,"pertence ao intervalo",a,",",b)
elif((x>b)or(a>x)):
	print(x,"nao pertence ao intervalo",a,",",b)