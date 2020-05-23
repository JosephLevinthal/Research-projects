# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
nome_patrono = input("nome:")

if (nome_patrono == "cervo"):
	msg = "cervo eh patrono do Harry Potter"
else:
	msg = nome_patrono + " nao eh patrono do Harry Potter"

print(msg)