# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
var1 = input("escreva patrono")
if (var1.lower() == "cervo"):
	mensagem = "cervo eh patrono do Harry Potter"
if (var1.lower() != "cervo"):
	mensagem = var1 + " nao eh patrono do Harry Potter"
print(mensagem)	