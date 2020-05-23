# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco = float(input("Informe o preco da compra:\n"))
if (preco>=200):
	print(round(preco - preco*(0.05),2))
else:
	print(preco)