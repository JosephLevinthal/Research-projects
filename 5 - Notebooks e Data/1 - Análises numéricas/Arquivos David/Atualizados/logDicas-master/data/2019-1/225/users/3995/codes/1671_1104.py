# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a=float(input("n1"))
b=float(input("n2"))
c=float(input("n3"))
d=float(input("n4"))
print("Intervalo 1:",a,",",b)
print("Intervalo 2:",c,",",d)
if(b>a and d>c):
	if(a>=c and a<=d):
		print("Ha intersecao")
	elif(b>=c and b<=d):
		print("Ha intersecao")
	elif(c>=a and c<=b):
		print("Ha intersecao")
	elif(d>=a and d<=b):
		print("Ha intersecao")
	else:
		print("Nao ha intersecao")
else:
	print("Entradas invalidas")