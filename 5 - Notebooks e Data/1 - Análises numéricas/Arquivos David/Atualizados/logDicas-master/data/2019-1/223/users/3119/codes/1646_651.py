altura = float(input("Altura da pessoa: "))
sexo = input("M ou F: ")
if(sexo == "M"):
	msg = (72.7 * altura) - 58
if(sexo == "F"):
	msg = (62.1 * altura) - 44.7

print(round(msg, 2))