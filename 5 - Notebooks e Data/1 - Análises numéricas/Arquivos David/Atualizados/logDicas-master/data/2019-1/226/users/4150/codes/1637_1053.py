# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

patrono = input("qual eh o patrono: ")

if (patrono.lower() == "cervo" ) :
	print("cervo eh patrono do Harry Potter")
else :
	a = patrono.lower()+ " nao eh patrono do Harry Potter"
	print(a)