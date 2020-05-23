# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco = float(input("preco a ser pago: "))

if preco < 200:
	print(round(preco,2))
else:
	precoff = preco - preco*(5/100)
	print(round(precoff,2))