# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco = float(input("Digite um numero:"))
desconto = 5/100
if (preco >= 200):
	pcd = preco - (preco * desconto)
	print(round(pcd,2))
else:
	print(round(preco,2))
	
