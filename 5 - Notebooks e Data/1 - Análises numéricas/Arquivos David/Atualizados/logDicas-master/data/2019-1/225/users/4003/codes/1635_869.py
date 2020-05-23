# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco = float(input("p: "))
des = preco - (preco*5/100)

if(preco >200):
	print(round(des,2))
else:
	print("preco")