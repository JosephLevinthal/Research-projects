ataque = input("Tipo de ataque TERRESTRE/AEREO/MARITIMO: ")
quant = int(input("Quantidade de unidades a serem destruidas: "))

if (quant > 0):
	if (ataque == "TERRESTRE"):
		dragao = "DROGON"
		unid = quant//150 + 1
		print(dragao)
		print(unid)
	elif(ataque == "AEREO"):
		dragao = "RHAEGAL"
		unid = quant//30 + 1
		print(dragao)
		print(unid)
	elif(ataque == "MARITIMO"):
		dragao = "VISERION"
		unid = quant//40 + 1
		print(dragao)
		print(unid)
	else:
		print("Entrada invalida")
else:
	print("Entrada invalida")