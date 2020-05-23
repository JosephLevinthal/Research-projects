# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

x=float(input("valo a ser pago: "))

if x >= 200:
	y = (x*5/100)
	mensagem = (x-y)
else:
	mensagem = (x)
	
print(round(mensagem,2))
