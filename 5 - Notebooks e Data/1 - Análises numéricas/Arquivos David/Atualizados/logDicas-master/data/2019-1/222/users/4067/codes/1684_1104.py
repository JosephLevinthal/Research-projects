a = float(input("ponto a: "))
b = float(input("ponto b: "))
c = float(input("ponto c: "))
d = float(input("ponto d: "))
print("Intervalo 1:",a,",",b)
print("Intervalo 2:",c,",",d)
if b > a and d > c:
	if (a <= d <=b) or (a<= c <= b):
		print("Ha intersecao")
	else:
		print("Nao ha intersecao")
else:
	print("Entradas invalidas")