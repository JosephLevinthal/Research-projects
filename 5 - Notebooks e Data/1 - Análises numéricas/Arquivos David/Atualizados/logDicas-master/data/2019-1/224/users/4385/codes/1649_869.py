# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
val=float(input("valor da compra"))
if val>=200:
	print(round(val-0.05 * val, 2))
else:
	print(round(val, 2))