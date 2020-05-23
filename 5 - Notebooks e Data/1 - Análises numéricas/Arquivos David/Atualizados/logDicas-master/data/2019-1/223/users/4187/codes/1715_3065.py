tipataq = input("tipo de ataque que o cornugon utilizou:").upper()
valdado = int(input("numero sorteado pelo dado de 4 faces:"))
numturnos = int(input("numero de turnos ate receber magia de cura:"))

if(tipataq != "CAUDA" or tipataq != "CUSPE" or tipataq != "PATADA" ) or (valdado != 1 and valdado != 2 and valdado != 3 and valdado != 4):
	print("Entrada invalida")
	
dano = 0
if(tipataq == "CAUDA" and (valdado >= 1 and valdado <= 4) ):
	dano = valdado * numturnos
	print(dano)
elif(tipataq == "CUSPE" and (valdado >= 1 and valdado <= 4)):
	dano = (2 * valdado) * numturnos
	print(dano)
elif(tipataq == "PATADA" and (valdado >= 1 and valdado <= 4)):
	dano = ((2 * valdado) - 5) * numturnos
	print(dano)
	