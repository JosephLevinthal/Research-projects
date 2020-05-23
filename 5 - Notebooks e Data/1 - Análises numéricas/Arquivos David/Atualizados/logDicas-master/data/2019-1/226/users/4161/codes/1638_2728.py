percurso = float(input("distancia: "))
tipo = input("tipo de carro (A/B): ")
t1 = percurso/8
t2 = percurso/12
if (tipo.upper() == "A"):
	print(round(t1, 2))
if (tipo.upper() == "B"):
	print(round(t2, 2))