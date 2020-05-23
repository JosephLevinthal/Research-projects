# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
valor = float(input(""))

if (valor >= 200):
	total = valor - ((valor * 5)/100)
	print(round(total,2))
else:
	total = valor
	print(round(total,2))