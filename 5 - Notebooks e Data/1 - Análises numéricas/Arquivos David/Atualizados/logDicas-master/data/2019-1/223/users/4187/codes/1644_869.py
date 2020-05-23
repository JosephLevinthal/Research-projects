# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

preço= float(input("valor da compra:"))

if(preço>=200):
	pc= preço - (preço*5/100)
	print(round(pc,2))
else:
	print(round(preço,2))