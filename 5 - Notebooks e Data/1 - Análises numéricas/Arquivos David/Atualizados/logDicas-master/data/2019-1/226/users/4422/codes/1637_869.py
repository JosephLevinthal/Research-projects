# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
comprasem = float(input("Valor da compra: "))

if(comprasem > 200.0):
	mensagem = comprasem - (comprasem * (5/100))
	
else:
	mensagem = comprasem
	
print(round(mensagem, 2))
