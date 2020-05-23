# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
p = input("patrono: ")

if (p != "cervo"):
	msg = " nao eh patrono do Harry Potter"
else:
	msg = " eh patrono do Harry Potter"
	
print(p + msg)