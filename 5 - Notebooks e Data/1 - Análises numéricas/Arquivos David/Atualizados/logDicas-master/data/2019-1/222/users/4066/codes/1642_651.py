altura = float(input('Altura em metros: '))
sexo = input('Sexo (M/F): ')

pesoM = (72.7)*altura - 58
pesoF = (62.1)*altura - 44.7

if (sexo == "M"):
	print(round(pesoM,2))
	
if (sexo == "F"):
	print(round(pesoF,2))