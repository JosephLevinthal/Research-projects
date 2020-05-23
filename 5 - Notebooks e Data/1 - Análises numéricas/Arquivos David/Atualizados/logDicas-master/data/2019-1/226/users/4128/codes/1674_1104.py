# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a = float(input (" a: "))
b = float(input (" b: "))
c = float(input (" c: "))
d = float(input (" d: "))

if(( a >= b) or (c >= d)):
	print("Intervalo 1:",a,",",b)
	print("Intervalo 2:",c,",",d)
	print("Entradas invalidas")
elif(b < c):
	print("Intervalo 1:",a,",",b)
	print("Intervalo 2:",c,",",d)
	print("Nao ha intersecao")
else:
	print("Intervalo 1:",a,",",b)
	print("Intervalo 2:",c,",",d)
	print("Ha intersecao")
	
	
	