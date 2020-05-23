nom1 = input("escreva o nome 1: ")
nome2 = input("escreva o nome 2: ")
if (nom1 < nom2):
	mensagem = nom1, nom2
else:
	mensagem = nom2, nom1
print(mensagem.upper())