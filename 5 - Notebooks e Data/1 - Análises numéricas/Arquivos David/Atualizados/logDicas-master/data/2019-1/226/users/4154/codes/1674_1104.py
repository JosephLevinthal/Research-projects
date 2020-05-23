# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a = float(input("um numero: "))
b = float(input("um numero: "))
c = float(input("um numero: "))
d = float(input("um numero: "))
print('Intervalo 1:',a,',',b)
print('Intervalo 2:',c,',',d)
if a<b and c<d:
	if b>=c:
		print('Ha intersecao')
	else:
		print('Nao ha intersecao')
else:
	print('Entradas invalidas')