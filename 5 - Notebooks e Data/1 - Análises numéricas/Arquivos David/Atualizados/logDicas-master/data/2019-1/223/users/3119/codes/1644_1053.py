# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

#Programa que leia o nome do patrono

p = input("Digite o nome: ")

if(p == "cervo"):
	mensagem = "cervo eh patrono do Harry Potter"
else: 
	mensagem = (p +" "+"nao eh patrono do Harry Potter")
	
print(mensagem)