x = float(input("Valor de x:"))
a = float(input("Valor de A:"))
b = float(input("Valor de B:"))
y = " pertence ao intervalo "

if(a>=b):
	print("Entradas",a," e ",b,"invalidas")
elif(a<=x)and(x<=b):
	print(x,y,a,",",b)
else:
	print(x," nao",y,a,",",b)