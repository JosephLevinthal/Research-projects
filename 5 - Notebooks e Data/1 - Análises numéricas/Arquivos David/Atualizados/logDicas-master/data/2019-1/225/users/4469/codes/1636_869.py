# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
compra = float(input("Preco sem desconto de uma compra: "))

if(compra >= 200.0):
	compra_com_desconto = compra - ((compra * 5) / 100)
else:
	compra_com_desconto = compra
	
print(round(compra_com_desconto, 2))