altura = float(input("digite altura: "))
sexo = input("digite sexo: ")

homens = (72.7*altura)-58
mulheres = (62.1*altura)-44.7

if(sexo=="M"):
	mensagem = homens
else:
	mensagem = mulheres

print(round(mensagem, 2))
			