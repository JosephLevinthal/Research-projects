PO = int(input("quantidade de pecas de ouro : "))
arma = input("nome da arma : ")
sucesso = int(input("fator de sucesso : "))
if(PO >= 100 and arma == "ESPADA"):
	dano = sucesso*10
	print(dano)
elif(PO >= 30 and arma == "MACHADO"):
	dano = sucesso+3
	print(dano)
elif(PO >= 50 and arma == "MARRETA"):
	dano = sucesso+5
	print(dano)
else:
	print("PO insuficiente")
	
	
	
	