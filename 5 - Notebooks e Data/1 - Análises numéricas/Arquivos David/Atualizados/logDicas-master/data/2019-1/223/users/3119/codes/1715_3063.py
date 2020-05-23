po = int(input("Quantidade de pecas de ouro: "))
nome = input("Nome da armadura: ")
des = int(input("Valor de destreza entre 1 e 8: "))

if(des < 1 and des > 8):
	print("Entrada invalida")
elif(po >= 50 and nome == "MALHA"):
	print(15 * des - 1)
elif(po < 50 and nome == "MALHA"):
	print("PO insuficiente")
elif(po >= 100 and nome == "PLACA"):
	print(20 * des - 18)
elif(po < 100 and nome == "PLACA"):
	print("PO insuficiente")
elif(po >= 100 and nome == "INTEIRA"):
	print(30 * des - 20)
elif(po < 100 and nome == "INTEIRA"):
	print("PO insuficiente")

