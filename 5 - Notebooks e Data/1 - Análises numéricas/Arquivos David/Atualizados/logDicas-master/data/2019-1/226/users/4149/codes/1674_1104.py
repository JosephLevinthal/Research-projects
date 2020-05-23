a=float(input("valor a "))
b=float(input("valor b   "))
c=float(input("valor c "))
d=float(input("valor d  "))
print("Intervalo 1:",a,",",b)
print("Intervalo 2:",c,",",d)
if((b>a)and(d>c)):
	if c>=a and c<=b:
		print("Ha intersecao")
	else:
		print("Nao ha intersecao")
else:
	print("Entradas invalidas")
	

