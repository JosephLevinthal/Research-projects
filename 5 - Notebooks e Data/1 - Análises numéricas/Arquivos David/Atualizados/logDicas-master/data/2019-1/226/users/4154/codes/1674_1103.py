# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input('qual o numero: '))
a = float(input('qual o numero: '))
b = float(input('qual o numero: '))

if a<b:
	if ((x>a) and (x<b)) or (x == a) or (x == b):
		print(x,'pertence ao intervalo',a,',',b)
	else:
		print(x,'nao pertence ao intervalo',a,',',b)
elif a>b:
	print('Entradas',a,'e',b,'invalidas')
		