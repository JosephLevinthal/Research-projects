# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

preco = float(input("preco total: "))

if preco < 200:
	print(preco)
else:
	preco = preco - (preco / 20)
	print(round(preco, 2))