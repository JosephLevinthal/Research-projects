# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
ent = input("qual o nome do patrono?")

if (ent.lower()=="cervo"):
	msg= ent + " eh patrono do Harry Potter"
else: 
	msg= ent+ " nao eh patrono do Harry Potter"
print(msg)