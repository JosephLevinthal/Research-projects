# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a=float(input("Valor de a: "))
b=float(input("Valor de b: "))
c=float(input("Valor de c: "))
d=float(input("Valor de d: "))
if((b<=a)or(d<=c)):
	print('Intervalo 1:', a, ',', b)
   print('Intervalo 2:', c, ',', d)
	print('Entradas invalidas')
elif(((c>=a)and(c<=b))or((d>=a)and(d<=b))):
	print('Intervalo 1:' a, ',', b)
	print('Intervalo 2:' c, ',', d)
	print('Entradas invalidas')
else:
	print('Intervalo 1: ', a, ',', b)
	print('Intervalo 2: ', c, ',', d)
	print('Nao ha intersecao')