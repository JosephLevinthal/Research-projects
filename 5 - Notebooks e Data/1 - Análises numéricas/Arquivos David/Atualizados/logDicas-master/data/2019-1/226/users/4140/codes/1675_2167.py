destino=input().upper()
percurso=input()
if(destino=="BELEM"):
	if(percurso=="ida"):
		print("350.0")
	elif(percurso=="ida-e-volta"):
		print("650.0")
	else:
		print("Destino inexistente")
elif(destino=="BORBA"):
	if(percurso=="ida"):
		print("80.0")
	elif(percurso=="ida-e-volta"):
		print("152.0")
	else:
		print("Destino inexistente")
elif(destino=="COARI"):
	if(percurso=="ida"):
		print("106.0")
	elif(percurso=="ida-e-volta"):
		print("199.0")
	else:
		print("Destino inexistente")
elif(destino=="HUMAITA"):
	if(percurso=="ida"):
		print("200.0")
	elif(percurso=="ida-e-volta"):
		print("390.0")
	else:
		print("Destino inexistente")
elif(destino=="MANICORE"):
	if(percurso=="ida"):
		print("150.0")
	elif(percurso=="ida-e-volta"):
		print("280.0")
	else:
		print("Destino inexistente")			
elif(destino=="MAUES"):
	if(percurso=="ida"):
		print("100.0")
	elif(percurso=="ida-e-volta"):
		print("190.0")
	else:
		print("Destino inexistente")
else:
	print("Destino inexistente")
	
