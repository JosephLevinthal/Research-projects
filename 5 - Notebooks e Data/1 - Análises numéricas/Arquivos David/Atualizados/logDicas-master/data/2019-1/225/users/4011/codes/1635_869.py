# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

compra = float(input("preco da compra: "))

if(compra >= 200):
	preco = - compra*0.05 + compra
else:
	preco = compra

print(round(preco, 2))