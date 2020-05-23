# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a = float(input("digite um valor: "))
b = float(input("digite um valor: "))
c = float(input("digite um valor: "))
d = float(input("digite um valor: "))
if((b>a) and (d>c)):
	if(((c>=a) and (c<=b)) or ((d>=a) and (d<=b))) or (((a>=c) and (b<=c)) or ((a>=d) and (b<=d))):	
		print("Intervalo 1:", a, ",",b)
		print("Intervalo 2:", c, ",",d)
		print("Ha intersecao")
	else:
		print("Intervalo 1:", a, ",",b)
		print("Intervalo 2:", c, ",",d)
		print("Nao ha intersecao")
else:
	print("Intervalo 1:", a, ",",b)
	print("Intervalo 2:", c, ",",d)
	print("Entradas invalidas")
	
	
