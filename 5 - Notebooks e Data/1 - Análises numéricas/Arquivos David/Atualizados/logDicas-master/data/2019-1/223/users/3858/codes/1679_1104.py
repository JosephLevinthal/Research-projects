# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.

a = float(input())
b = float(input())
c = float(input())
d = float(input())

if(b>a and d>c):
	if((a>=c and a<d) or (b>=c and b<d) or (c>=a and c<b) or (d>=a and d<b) ):
		print("Intervalo 1: ",a, " , ", b)
		print("Intervalo 2: ",c, ",", d)
		print("Ha intersecao")
	else:
		print("Intervalo 1: ",a, " , ", b)
		print("Intervalo 2: ",c, ",", d)
		print("Nao ha intersecao")
else:
	print("Intervalo 1: ",a, " , ", b)
	print("Intervalo 2: ",c, ",", d)
	print("Entradas invalidas")
