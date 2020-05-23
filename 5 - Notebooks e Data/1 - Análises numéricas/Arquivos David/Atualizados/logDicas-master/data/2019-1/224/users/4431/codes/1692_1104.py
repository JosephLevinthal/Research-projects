a=float(input("Digite o valor a :"))
b=float(input("Digite o valor b :"))
c=float(input("Digite o valor c :"))
d=float(input("Digite o valor d :"))
print("Intervalo 1:",a,",",b)
print("Intervalo 2:",c,",",d)
if(a>=b)or(c>=d):
	print("Entradas invalidas")
elif((c>=a)and(c<=b))or(d>=a and d<=b):
	print("Ha intersecao")
else:
	print("Nao ha intersecao")
