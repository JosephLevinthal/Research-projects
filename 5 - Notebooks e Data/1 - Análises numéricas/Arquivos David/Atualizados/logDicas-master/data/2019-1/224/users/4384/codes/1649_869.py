# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco=float(input("digite o preco sem descontos:    "))
if(preco>=200):
	x=preco-preco*0.05
	print(round(x,2))
else:
	print(round(preco,2))