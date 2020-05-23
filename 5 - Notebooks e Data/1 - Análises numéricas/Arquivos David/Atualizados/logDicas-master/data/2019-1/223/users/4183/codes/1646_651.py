altura = float(input("Digite a altura: ")) 
sexo = input("Digite o sexo: ")
M = (72.7 * altura) - 58
F = (62.1 * altura) - 44.7
if (sexo == "M"):
	print(round(M,2))
else:
	print(round(F,2))
			
