x= float(input("insira um numero x: "))
a= float(input("insira o primeiro numero: "))
b= float(input("insira o segundo numero: "))
if b>a:
	if (x>=a)and(x<=b):
		print(x,"pertence ao intervalo",a,",",b)
	elif not((x>=a)and(x<=b)):
		print(x,"nao pertence ao intervalo",a,",",b)
else:
	print("Entradas",a,"e",b,"invalidas")
