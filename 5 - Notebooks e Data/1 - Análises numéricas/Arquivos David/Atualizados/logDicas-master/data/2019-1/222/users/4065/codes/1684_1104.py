# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a = float(input("numero: "))
b = float(input("numero: "))
c = float(input("numero: "))
d = float(input("numero: "))



if(b < a) or (d < c):
	print("Intervalo 1:",a,",",b)
	print("Intervalo 2:",c,",",d)
	print("Entradas invalidas")
	


else:
	if((a < b) and (b > a)) == ((b < c) and (c > b)) and ((c < d) and (d > c)):
		print("Intervalo 1:",a,",",b)
		print("Intervalo 2:",c,",",d)
		print("Ha intersecao")
	else:
		print("Nao ha intersecao")