percurso = float(input("Insira o percurso: "))
tipo = input("Tipo do carro: ")
if(tipo == "A"):
	consumo = percurso/8
	print(round(consumo,2))
else:
	consumo = percurso/12
	print(round(consumo,2))