
po = int(input("Digite po: "))
arma = input("Digite arma: ").upper()
d = int(input("Digite dano: "))



if(d >=1 and d <=10 and arma=="ESPADA" or arma=="MARRETA" or arma=="MACHADO"):
	if(arma == "ESPADA"):
		if(po>=100):
			dano = d*10
			print(dano)
		else:
			print("PO insuficiente")
	elif(arma == "MACHADO"):
		if(po>=30):
			dano = d+3
			print(dano)
		else:
			print("PO insuficiente")
	elif(arma == "MARRETA"):
		if(po>=50):
			dano = d+5
			print(dano)
		else:
			print("PO insuficiente")
else:
	print("Entrada invalida")
		