# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco = float(input("valor da comprar: "))
if (preco >= 200.00):
	preco = preco * 0.95
	print(round(preco,2))
	