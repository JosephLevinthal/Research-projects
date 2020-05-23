# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
entrada = input("nome do patronum: ")
if (entrada == "cervo"):
	msg=("cervo eh patrono do Harry Potter")
else:
   msg=(entrada + " nao eh patrono do Harry Potter")
print(msg)