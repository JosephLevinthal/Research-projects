# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
compra = float(input("total: "))
desconto = compra * 5 / 100
nota = compra - desconto
if (compra>=200):
	print(round(nota,2))
else:
	print(round(compra,2))