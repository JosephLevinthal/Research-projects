# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a = float(input('Insira um valor para a: '))
b = float(input('Insira um valor para b: '))
c = float(input('Insira um valor para c: '))
d = float(input('Insira um valor para d: '))
print('Intervalo 1:', a,',', b)
print('Intervalo 2:', c,',', d)

if ((b>a) and (d>c)):
	if ((a<=c and b>=c) or (c<=a and b<=c) or (d>=a and b>=d) or (d<=a and d>=b)):
		print('Ha intersecao')
	else:
		print('Nao ha intersecao')
else:
	print('Entradas invalidas')
	