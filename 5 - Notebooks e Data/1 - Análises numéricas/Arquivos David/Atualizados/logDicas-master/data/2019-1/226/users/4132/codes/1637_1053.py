# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

patrono = input("Digite um patrono: ")

if( patrono.lower() == "cervo"):
	mensagem = patrono.lower() + " eh patrono do Harry Potter"
else:
	mensagem = patrono.lower() + " nao eh patrono do  Harry Potter"
	
print(mensagem)