# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
num = float(input("valor"))
if (num >= 200):
	preco = num - (5/100) * num
else:
	preco = num
print(round(preco, 2))
	
	
	