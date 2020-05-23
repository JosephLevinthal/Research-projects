ta = input("tipo de ataque: (TERRESTRE/AEREO/MARITIMO)")
qnt = int(input("quantidade de unidades dstruidas:"))
if(qnt>0):
	if(ta.upper() == "TERRESTRE"):
		print("DRAGON")
		print((qnt//150)+1)
	elif(ta.upper() == "AEREO"):
		print("RHAEGAL")
		print((qnt//30)+1)
	elif(ta.upper() == "MARITIMO"):
		print("VISERION")
		print((qnt//40)+1)
else:
	print("Entrada invalida")