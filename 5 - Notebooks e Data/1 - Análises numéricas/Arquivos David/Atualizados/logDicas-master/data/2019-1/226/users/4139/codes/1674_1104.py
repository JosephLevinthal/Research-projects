a = float(input("valor de A:"))
b = float(input("valor de B:"))
c = float(input("valor de C:"))
d = float(input("valoe de D:"))

print("Intervalo 1: ",a,",",b)
print("Intervalo 2: ",c,",",d)

if(b<=a)or(d<=c):
	print("Entradas invalidas")
elif(b<c):
	print("Nao ha intersecao")
else:
	print("Ha intersecao")