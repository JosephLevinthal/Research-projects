percurso = float(input("o percurso de uma viagem (em quilometros): "))
tipo = input("o tipo do carro (A ou B): ")

if tipo.upper() == "A": 
	consumo = percurso / 8
	print(round(consumo, 2))
else :
	consumo = percurso / 12
	print(round(consumo, 2))