x=float(input("Digite o valor x: "))
a=float(input("Digite o valor a: "))
b=float(input("Digite o valor b: "))
if(b<=a):
	print("Entradas",a,"e",b,"invalidas")
elif(x>=a)and(x<=b):
	print(x,"pertence ao intervalo",a,",",b)
else:
   print(x,"nao pertence ao intervalo",a,",",b)	
