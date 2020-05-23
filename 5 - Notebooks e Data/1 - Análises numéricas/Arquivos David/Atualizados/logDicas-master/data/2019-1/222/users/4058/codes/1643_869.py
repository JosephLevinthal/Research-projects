# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
compra=float(input('valor da compra?'))
if(compra>=200):
	desconto=compra*(95/100)
	print(round(desconto, 2))
else:
	print(round(compra, 2))