x=float(input("primeira entrada:"))
a=float(input("segunda entrada:"))
b=float(input("terceira entrada:"))
if(b>a):
	if(x>=a and x<=b):
		print(x, "pertence ao intervalo",a,",",b)
	else:
		print(x,"nao pertence ao intervalo",a,",",b)
else:
		print("Entradas",a,"e",b,"invalidas")

