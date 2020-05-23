a=float(input("a"))
b=float(input("b"))
c=float(input("c"))
d=float(input("d"))

	
if(b>a and d>c):
	
	if(a==c or b==d or a==d or b==c):
		print("Intervalo 1:", a, ",", b)
		print("Intervalo 2:", c, ",", d)
		print("Ha intersecao")

	if(a!=c or b!=d or a!=d or b!=c):
		print("Intervalo 1:", a, ",", b)
		print("Intervalo 2:", c, ",", d)
		print("Nao ha intersecao")

	
else:
	print("Intervalo 1:", a, ",", b)
	print("Intervalo 2:", c, ",", d)
	print("Entradas invalidas")
	
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
