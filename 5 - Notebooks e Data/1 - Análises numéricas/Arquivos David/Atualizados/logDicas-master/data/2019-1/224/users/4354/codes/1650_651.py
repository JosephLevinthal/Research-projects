altura = float(input("altura em metros: "))
sexo = input("sexo: ")
sexo = sexo.upper()
if(sexo == "M") :
	peso = (72.7 * altura) - 58
	print(round(peso,2))
	
if(sexo == "F") :
	peso = (62.1 * altura) - 44.7
	print(round(peso,2))
	
