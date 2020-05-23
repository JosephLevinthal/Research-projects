tempo = float(input("Tempo de voo: "))
tempoex = (tempo - 200)
if (tempo < 200):
	valor = 5000 + 100*tempo
	print(round(valor,2))

else:
	valor = 8000 + 100*200 + 90*tempoex
	print(round(valor,2))