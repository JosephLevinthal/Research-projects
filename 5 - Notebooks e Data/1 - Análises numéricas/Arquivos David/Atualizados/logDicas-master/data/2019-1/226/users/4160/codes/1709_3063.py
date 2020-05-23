po = int(input("A quantidade de pecas de ouro: "))
a = input("Nome da armadura (MALHA, PLACA ou INTEIRA): ").upper()
d = int(input("Fator de destreza: "))

if ((d <=0 or d >8) and (a!= "MALHA" or a!= "PLACA" or a!= "INTEIRA")):
	print("Entrada invalida")
elif(po < 50) :
	print("PO insuficiente")
elif (a == "INTEIRA" and po >= 200):
	r = (30 * d) - 20 
	print (r)
elif (a== "MALHA" and po >= 50 or po < 100):
	r = (15 * d) - 1
	print(r)
elif (a=="PLACA" and po >=100 or po < 200):
	r = (20 * d) - 18
	print(r)

	


	