# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
patrono = input("Qual o pattrono:")
if (patrono.lower() == "cervo"):
	msg = patrono +" " + "eh patrono do Harry Potter"
else:
	msg = patrono + " " + "nao eh patrono do Harry Potter"
print(msg)	