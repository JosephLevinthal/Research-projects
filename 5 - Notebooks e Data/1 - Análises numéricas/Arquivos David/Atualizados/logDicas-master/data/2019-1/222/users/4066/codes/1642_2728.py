percurso = float(input("Percurso: "))
tipo = input("Carro A ou B: ")

consumoA = percurso/8
consumoB = percurso/12

if (tipo.upper() == "A"):
	print(round(consumoA,2))
	
if (tipo.upper() == "B"):
	print(round(consumoB,2))