# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
compra=float(input("Valor da compra: "))
if (compra>=200):	
	mensagem= compra - (5/100)*compra
else:
	mensagem= compra
	
print(round(mensagem ,2))	