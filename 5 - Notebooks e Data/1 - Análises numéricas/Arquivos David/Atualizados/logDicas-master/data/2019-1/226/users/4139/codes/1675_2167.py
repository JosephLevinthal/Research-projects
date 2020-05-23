n = input("nome da cidade de destino: ").upper()
m = input("ida ou ida-e-volta: ").upper()

if(n == "BELEM"):
	if(m == "IDA"):
		print("350.0")
	else:
		print("650.0")
elif(n == "BORBA"):
	if(m == "IDA"):
		print("80.0")
	else:
		print("152.0")
elif(n == "COARI"):
	if(m == "IDA"):
		print("106.0")
	else:
		print("199.0")
elif(n == "HUMAITA"):
	if(m == "IDA"):
		print("200.0")
	else:
		print("390.0")
elif(n == "MANICORE"):
	if(m == "IDA"):
		print("150.0")
	else:
		print("280.0")
elif(n == "MAUES"):
	if(m == "IDA"):
		print("100.0")
	else:
		print("190.0")
else:
	print("Destino inexistente")