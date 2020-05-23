# Definindo a cidade de destino:
cd = input("Digite a cidade de destino: ")
pc = input("Percurso somente ida ou ida-e-volta? ")
cd = cd.lower()
pc = pc.lower()

#Calculo do valor da passagem:
if(cd == "belem") and (pc == "ida"):
	print(350.0)
elif(cd == "belem") and (pc == "ida-e-volta"):
	print(650.0)
elif(cd == "borba") and (pc == "ida"):
	print(80.0)
elif(cd == "borba") and (pc == "ida-e-volta"):
	print(152.0)	
elif(cd == "coari") and (pc == "ida"):
	print(106.0)
elif(cd == "coari") and (pc == "ida-e-volta"):
	print(199.0)	
elif(cd == "humaita") and (pc == "ida"):
	print(200.0)
elif(cd == "humaita") and (pc == "ida-e-volta"):
	print(390.0)
elif(cd == "manicore") and (pc == "ida"):
	print(150.0)
elif(cd == "manicore") and (pc == "ida-e-volta"):
	print(280.0)
elif(cd == "maues") and (pc == "ida"):
	print(100.0)
elif(cd == "maues") and (pc == "ida-e-volta"):
	print(190.0)
else:
	print("Destino inexistente")
	