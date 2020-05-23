percurso = float(input("digite o percurso em km: "))
tipo = input("carro A ou B: ")

carroA = percurso / 8
carroB = percurso / 12
tipo = tipo.lower()
if(tipo == "a"):
	print(round(carroA,2))
if(tipo == "b"):
	print(round(carroB,2))
