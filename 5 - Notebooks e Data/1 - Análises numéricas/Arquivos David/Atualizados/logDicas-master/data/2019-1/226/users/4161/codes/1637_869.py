# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco = float(input("valor da compra: "))
if (preco >= 200.00):
	print(round(preco - preco*0.05, 2))
else:
	print(round(preco, 2))