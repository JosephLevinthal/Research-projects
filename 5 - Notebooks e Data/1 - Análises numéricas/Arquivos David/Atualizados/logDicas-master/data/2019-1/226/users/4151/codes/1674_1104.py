a=float(input("num1: "))
b=float(input("num1: "))
c=float(input("num1: "))
d=float(input("num1: "))
print("Intervalo 1: ",a,",",b)
print("Intervalo 2: ",c,",",d)

if((b<=a)or(d<=c)):
	print("Entradas invalidas")
elif(b<c):
	print("Nao ha intersecao")
else:
	print("Ha intersecao")
	

