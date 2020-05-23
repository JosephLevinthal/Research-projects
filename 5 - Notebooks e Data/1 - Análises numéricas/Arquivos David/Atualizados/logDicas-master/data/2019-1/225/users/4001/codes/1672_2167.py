D = input("Destino: ")
P = input("Percuso ida/ida-e-volta? ")

if (D == "Belem"):
	if (P == "ida"):
		print(350.0)
	else:
		print(650.0)
elif (D == "Borba"):
	if (P == "ida"):
		print(80.0)
	else:
		print(152.0)
elif (D == "Coari"):
	if (P == "ida"):
		print(106.0)
	else:
		print(199.0)
elif (D == "Humaita"):
	if (P == "ida"):
		print(200.0)
	else:
		print(390.0)
elif (D == "Manicore"):
	if (P == "ida"):
		print(150.0)
	else:
		print(280.0)
elif (D == "Maues"):
	if (P == "ida"):
		print(100.0)
	else:
		print(190.0)
else:
	print("Destino inexistente")