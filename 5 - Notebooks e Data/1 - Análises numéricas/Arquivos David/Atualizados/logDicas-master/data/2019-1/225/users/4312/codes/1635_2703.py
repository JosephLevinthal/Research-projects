idade = int(input("digite a idade: "))

if (idade >= 18):  
	mensagem = "Eleitor"
else:
	mensagem = "nao_eleitor"
print(mensagem.lower())