# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a = float(input("escreva o valor de a: "))
b = float(input("escreva o valor de b: "))
c = float(input("escreva o valor de c: "))
d = float(input("escreva o valor de d: "))
print ("Intervalo 1:",a,",",b)
print ("Intervalo 2:",c,",",d)
if (b > a) and (d > c):
	if ((b >=c) and (d >= a) or (d >=a) and (b >=c)):
		print ("Ha intersecao")
	else:
		print ("Nao ha intersecao")
else:
	print ("Entradas invalidas")
	
