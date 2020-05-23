# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preço = float(input("valor de compra:"))

if (preço >= 200):
	preço = preço - (preço*5/100) 
else:
	preço = preço
print (round (preço , 2)) 
