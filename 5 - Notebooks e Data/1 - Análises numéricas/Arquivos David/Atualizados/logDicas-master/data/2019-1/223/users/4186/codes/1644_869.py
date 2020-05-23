# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco= float(input("valor da compra: "))
desconto= (preco*5)/100
if (preco>=200):
	print(round(preco-desconto,2))
else:
	print(round(preco,2))