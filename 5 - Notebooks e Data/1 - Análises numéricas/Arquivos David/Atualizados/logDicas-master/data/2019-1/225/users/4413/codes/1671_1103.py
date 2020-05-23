x=float(input("numero: "))
a=float(input("numero: "))
b=float(input("numero: "))

if(b<=a):
	print("Entradas",a,"e",b,"invalidas")
elif(a<=x)and(x<=b):
	print(x,"pertence ao intervalo",a,",",b)
else:
	print(x,"nao pertence ao intervalo",a,",",b)