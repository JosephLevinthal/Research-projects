# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco = float(input("insira o preco da compra: "))

if (preco <= 200):
	mensagem = preco
else:
	mensagem = preco - (preco * 5/100)
	
print(round(mensagem,2))