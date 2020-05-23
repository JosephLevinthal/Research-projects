# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco = float(input("valor de compra:")) 

if (preco >= 200): 
	preco = preco - (preco*5/100) 
else:
	preco = preco 
print (round (preco , 2))