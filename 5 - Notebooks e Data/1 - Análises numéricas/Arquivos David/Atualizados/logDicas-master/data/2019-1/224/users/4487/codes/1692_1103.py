x=float(input("x:   "))
a=float(input("a:   "))
b=float(input("b:   "))
if(b>a):
	if(x<=b)and(x>=a):
		print(x,"pertence ao intervalo ",a,", ",b)
	else:
		print(x,"nao pertence ao intervalo ",a,", ",b)
else:
	print("Entradas ",a," e ",b," invalidas")