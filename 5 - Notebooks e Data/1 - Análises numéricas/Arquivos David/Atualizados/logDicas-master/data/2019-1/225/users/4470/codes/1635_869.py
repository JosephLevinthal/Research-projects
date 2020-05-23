# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco = float(input())

if (preco>=200):
	x = preco-(5/100)*preco
	
else:
	x = preco
	
print(round(x, 2))