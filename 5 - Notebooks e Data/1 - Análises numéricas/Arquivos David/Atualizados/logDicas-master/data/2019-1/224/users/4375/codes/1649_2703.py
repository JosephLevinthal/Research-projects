leitor = int(input("Digite a sua idade: "))
if(leitor >= 18):
	mensagem = "eleitor"
	print(mensagem.lower())
else:
	mensagem = "nao_eleitor"
	print(mensagem.lower())