# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a= float(input("Insira o intervalo A:"))
b= float(input("Insira o intervalo B:"))
c= float(input("Insira o intervalo C:"))
d= float(input("Insira o intervalo D:"))

if (b>a and d>c):
	if((c >= a and c <= b) or (d>=a and d<=b)):
		print("Intervalo 1:", a,",", b)
		print("Intervalo 2:", c,",",d)
		print("Ha intersecao")
	else:
		print("Intervalo 1:", a,",", b)
		print("Intervalo 2:", c,",",d)
		print("Nao ha intersecao")
else:
	print("Intervalo 1:", a,",", b)
	print("Intervalo 2:", c,",",d)
	print("Entradas invalidas")