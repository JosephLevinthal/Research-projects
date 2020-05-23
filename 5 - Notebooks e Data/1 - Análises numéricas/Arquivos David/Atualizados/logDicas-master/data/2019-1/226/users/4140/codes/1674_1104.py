a=float(input())
b=float(input())
c=float(input())
d=float(input())
if(b<a or d<c):
	print("Intervalo 1:",a,",", b)
	print("Intervalo 2:",c,",", d)
	print("Entradas invalidas")
else:
	
	if(a<c and b<c) or( a>d and b>d):
		print("Intervalo 1:",a,",", b)
		print("Intervalo 2:",c,",", d)
		print("Nao ha intersecao")
	else:
		print("Intervalo 1:",a,",", b)
		print("Intervalo 2:",c,",", d)
		print("Ha intersecao")
		
	
