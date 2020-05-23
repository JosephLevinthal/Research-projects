# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco = float(input("Qual o valor? "))

if(preco >= 200.0):
	mensagem = preco - (preco * (5/100))
	
else:
	mensagem = preco
	
print(round(mensagem, 2))