# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
ep= input("escreva seu patronum: ")

if (ep.upper()=="CERVO"):
	msg="cervo eh patrono do Harry Potter"
if (ep.upper()!= "CERVO"):
	msg= ep+" nao eh patrono do Harry Potter"

print(msg)

