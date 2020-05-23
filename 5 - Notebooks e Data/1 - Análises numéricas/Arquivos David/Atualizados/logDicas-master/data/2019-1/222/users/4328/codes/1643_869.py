# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco = float(input())

if (preco >= 200):
	mensagem = (preco - (0.05 * preco) )
else:
	mensagem = (preco)
	
print(round(mensagem,2))
	