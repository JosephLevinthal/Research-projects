PO = int(input("digite: "))
armadura = input("digite: ")
d = int(input("digite: "))

if ((PO == 200) and (PO == 50) and (PO == 100)):
	if((PO == 200) and (armadura == "INTEIRA")):
		res = (30 * d) - 20
		print(res)
	elif ((PO == 50) and (armadura == "MALHA")):
		res = (15 * d) - 1
		print(res)
	elif ((PO == 100) and  (armadura == "PLACA")):
		res = (20 * d)- 18
		print(res)

else:
	print("PO insuficiente")
