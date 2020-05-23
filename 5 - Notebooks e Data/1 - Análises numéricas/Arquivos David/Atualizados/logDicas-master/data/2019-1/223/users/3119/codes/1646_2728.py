percurso = float(input("Distancia percorrida: "))
tipo = input("Qual o tipo do carro? A ou B? ")

if(tipo == "A"):
	msg = percurso / 8
if(tipo == "B"):
	msg = percurso / 12

print(round(msg, 2 ))