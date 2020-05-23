tipo= input("ESPADA OU CAUDA?: ").upper
dd1= int(input("Dado 1: "))
dd2= int(input("Dado 2: "))
dd3= int(input("Dado 3: "))
dd4= int(input("Dado 4: "))

if (tipo == ("CAUDA" or "cauda") and (dd1 <= 6) or (dd2 <= 6) or (dd3 <= 6) or (dd4 <= 6)):
	fcauda= (dd1 + dd2 + dd3) * dd4
	print(fcauda)
	
elif (tipo == ("ESPADA" or "espada") and (dd1 <= 6) or (dd2 <= 6) or (dd3 <= 6) or (dd4 <= 6)):
	fespada= (dd1 + dd2 + dd3 + dd4)
	print(fespada + 24)
	
elif (tipo != ("ESPADA" or "espada") or (dd1 > 6) or (dd2 > 6) or (dd3 > 6) or (dd4 > 6)): 
	print("Entrada invalida")
	
elif (tipo != "CAUDA" or "cauda") or dd1 > 6 or dd2 > 6 or dd3 > 6 or dd4 > 6:
	print("Entrada invalida")
	
		
