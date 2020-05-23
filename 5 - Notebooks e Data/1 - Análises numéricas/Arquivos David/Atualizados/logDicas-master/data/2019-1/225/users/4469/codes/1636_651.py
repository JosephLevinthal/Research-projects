altura = float(input())
sexo = input()

if(sexo.upper() == "M"):
	peso_ideal = (72.7 * altura) - 58
else:
	peso_ideal = (62.1 * altura) - 44.7
	
print(round(peso_ideal, 2))