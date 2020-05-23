a = float(input("Valor de A: "))
b = float(input("Valor de B: "))
c = float(input("Valor de C: "))
d = float(input("Valor de D: "))

print("Intervalo 1: ",a,",",b)
print("Intervalo 2: ",c,",",d)

if(b <= a) or (d <= c):
	print("Entradas invalidas")
elif(b < c):
	print("Nao ha intersecao")
else:
	print("Ha intersecao")