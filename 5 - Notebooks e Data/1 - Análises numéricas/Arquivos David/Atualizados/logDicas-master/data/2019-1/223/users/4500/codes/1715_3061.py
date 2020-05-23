var = input("Insira o tipo de ataque: ")
quat = int("Insira a quantidade a ser destruida: ")

if (quat < 0):
	tipo = "Entrada invalida"
elif(var == TERRESTRE):
	tipo = "DROGON"
	ataque(150 / quat)
elif(var == AEREO):
	tipo = "Rhaegal"
	ataque (30 / quat)
elif(var == MARITIMO):
	tipo = "Viserion"
	ataque(40 / quat)
print (tipo)
print(ataque)
	