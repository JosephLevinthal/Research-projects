# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco=float(input("preco da compra: "))
preco_minimo=200
if (preco>=200):
	print(round(preco*0.95,2))
else:
	print(round(preco,2))
