# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a=float(input(""))
b=float(input(""))
c=float(input(""))
d=float(input(""))

if(b>a and d>c):
	if(a<d<b or a<c<b or a<d<c<b or c<a<d or c<b<d or c<a<b<d ):
		print("Intervalo 1:", a, ",", b)
		print("Intervalo 2:", c, ",", d)
		print("Ha intersecao")
	else:
		print("Intervalo 1:", a, ",", b)
		print("Intervalo 2:", c, ",", d)
		print("Nao ha intersecao")
else:
	print("Intervalo 1:", a, ",", b)
	print("Intervalo 2:", c, ",", d)
	print("Entradas invalidas")
		