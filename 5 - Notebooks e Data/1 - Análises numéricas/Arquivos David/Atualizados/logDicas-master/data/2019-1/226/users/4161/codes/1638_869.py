# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código
compra = float(input("valor da compra: "))
if (compra >= 200.00):
	print(round(compra*0.95, 2))
else:
	print(round(compra, 2))