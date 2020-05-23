# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
compra = float(input('Valor da compra: '))

if compra>=200:
	r = (compra*(5/100))
	s = compra - r
	print(round(s, 2))
else:
	print(compra)