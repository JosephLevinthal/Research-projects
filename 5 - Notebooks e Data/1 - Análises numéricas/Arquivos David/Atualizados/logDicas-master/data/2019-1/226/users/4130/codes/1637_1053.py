# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

ent = input("Patrono: ")

if (ent.lower() == "cervo" ):
	mensagem = ent + " eh patrono do Harry Potter"
else:
	mensagem = ent + " nao eh patrono do Harry Potter"

print(mensagem)