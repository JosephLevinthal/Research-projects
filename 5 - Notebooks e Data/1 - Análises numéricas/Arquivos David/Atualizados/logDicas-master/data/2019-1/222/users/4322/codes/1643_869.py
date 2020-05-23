# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
compra = float(input("valor da compra? "))
desconto = compra * 5 / 100
preco_a_pagar = compra - desconto
if (compra >= 200):
	print(round(preco_a_pagar, 2))
else:
	print(round(compra, 2))
	