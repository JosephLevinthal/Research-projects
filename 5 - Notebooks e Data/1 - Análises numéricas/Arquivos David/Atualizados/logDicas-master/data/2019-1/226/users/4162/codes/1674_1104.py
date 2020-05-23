a= float(input("insira o numero a: "))
b= float(input("insira o numero b: "))
c= float(input("insira o numero c: "))
d= float(input("insira o numero d: "))

if (b>a)and(d>c):
	if ((c>=a)and(c<=b))or((d>=a)and(d<=b)):
		print("Intervalo 1:",a,",",b)
		print("Intervalo 2:",c,",",d)
		print("Ha intersecao")
	else:
		print("Intervalo 1:",a,",",b)
		print("Intervalo 2:",c,",",d)
		print("Nao ha intersecao")
else:
	print("Intervalo 1:",a,",",b)
	print("Intervalo 2:",c,",",d)
	print("Entradas invalidas")