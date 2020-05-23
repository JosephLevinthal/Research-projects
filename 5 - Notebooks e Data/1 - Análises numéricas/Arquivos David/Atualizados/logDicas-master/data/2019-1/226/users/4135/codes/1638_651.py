h = float(input("Digite a altura:"))
sexo = input ("Digite o sexo da pessoa?(M/H) ")
mulheres = (62.1*h)-44.7
if (sexo =="M"):
	homens = (72.7*h)-58
	print (round(homens,2))
else:
	mulheres = (62.1*h)-44.7
	print (round(mulheres,2))