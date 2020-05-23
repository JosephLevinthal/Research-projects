altura = float(input(" Digite a altura "))
sexo = input(" M/F? ")
if(sexo== "M"):
	mensagem = ((72.7) * altura)- 58
	print(round(mensagem,2))
	
else:
	mensagem = ((62.1) * altura)- 44.7
	print(round(mensagem,2))
	