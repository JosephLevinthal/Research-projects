# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
valor_compra = float(input("Digite o valor da compra:"))
if (valor_compra>=200):
	print (round(valor_compra*0.95,2))
else:
	print(round(valor_compra,2))
