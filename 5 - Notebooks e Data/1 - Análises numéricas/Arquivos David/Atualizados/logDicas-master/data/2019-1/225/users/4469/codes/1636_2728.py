percurso = float(input("Percurso: "))
tipoCarro = input("Tipo do carro: ")

if(tipoCarro.upper() == "A"):
	consumo = percurso / 8
else:
	consumo = percurso / 12
	
print(round(consumo, 2))