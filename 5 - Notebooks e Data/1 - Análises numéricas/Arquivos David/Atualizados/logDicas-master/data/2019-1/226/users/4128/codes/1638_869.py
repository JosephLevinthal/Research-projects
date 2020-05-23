# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco = float(input("valor: "))

if(preco >= 200):
	desc = (preco * 5) /100
	desc1 = preco - desc
	print(round(desc1,2))
else:
	print(round(preco,2))
