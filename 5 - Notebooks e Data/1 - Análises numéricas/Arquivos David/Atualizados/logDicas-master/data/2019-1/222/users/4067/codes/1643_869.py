# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
compra = float(input("valor das compras: "))
if compra >= 200:
	mensagem = compra - (compra* 5/100)
else:
	mensagem = compra
print(round(mensagem,2))