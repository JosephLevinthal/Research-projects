a = input("digite qual foi o ataque: ").upper()
b = int(input("digite a numeracao do dado: "))
c = int(input("digite a numeracao do segundo dado: "))
if(b<1) or (b>8) and (c<1) or (c>8):

	if(b == "FURIA"):
		x = (10 + b * 2)
	elif(b == "GRITO"):
		x = (6 + b * 2)
	elif(b == "TOQUE"):
		x = (b * 2 + c * 2)
else:
	print(x)
		
	
		


		