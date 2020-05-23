x=input("Digite a cidade de destino : ")
y=input("Digite se e ida/ida-e-volta: ")
if(x!="Belem")and(x!="Borba")and(x!="Coari")and(x!="Humaita")and(x!="Manicore")and(x!="Maues"):
	print("Destino inexistente")
elif(x=="Belem"):
	if(y=="ida"):
		print("350.00")
	else:
		print("650.00")
elif(x=="Borba"):
	if(y=="ida"):
		print("80.00")
	else:
		print("152.00")
elif(x=="Coari"):
	if(y=="ida"):
		print("106.00")
	else:
		print("199.00")
elif(x=="Humaita"):
	if(y=="ida"):
		print("200.00")
	else:
		print("390.00")
elif(x=="Manicore"):
	if(y=="ida"):
		print("150.00")
	else:
		print("280.00")
elif(x=="Maues"):
	if(y=="ida"):
		print("100.00")
	else:
		print("190.00")