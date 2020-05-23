po = int(input("quantidade de pecas de ouro: "))
na = input("nome da armadura: ").upper()
d = int(input("destreza sorteada no dado: "))
if((d<=8)and(d>=1)or(na!="INTEIRA")or(na!="PLACA")or(na!="MALHA")):
	if((po<50)or(po<100)and(na=="PLACA")or(po<200)and(na=="INTEIRA")):
		print("PO insuficiente")
	elif(na=="INTEIRA"):
		  da=30*d -20
		  print(da)
	elif(na=="MALHA"):	
		  da=15*d -1
		  print(da)
	elif(na=="PLACA"):
		  da= 20*d-18
		  print(da)
else:
	print("Entrada invalida")