PO=int(input("pecas:"))
na=input("ESPADA/MACHADO/MARRETA").upper()
d=int(input("valor do dado:"))
if(d>=1 and d<=10):
	if(na=="ESPADA" or na=="MACHADO" or na=="MARRETA"):
		if(PO>=100):
			if(na=="ESPADA"):
				dano=d*10
				print(dano)
			elif(na=="MACHADO"):
				dano=d+3
				print(dano)
			else:
				dano=d+5
		elif(PO>=30 and PO<=99):
			if(na=="MACHADO"):
				dano=d+3
				print(dano)
			elif(na=="MARRETA"):
				dano=d+5
				print(dano)
			else:
				print("PO insuficiente")
		elif(PO>=30 and PO<=49):
			if(na=="MACHADO"):
				dano=d+3
				print(dano)
			else:
				print("PO insuficiente")
		elif(PO==30):
			if(na=="MACHADO"):
				dano=d+3
				print(dano)
			else:
				print("PO insuficiente")
		else:
			print("PO insuficiente")
	else:
		print("Entrada invalida")
else:
	print("Entrada invalida")