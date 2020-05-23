#Valor da cedula
c = int(input("digite o valor da cedula: "))

if(c==2) or (c==5) or (c==10) or (c==20) or (c==50) or (c==100):
	
	print("Entrada: ", c)
	
	if(c==2):
		print("Animal: Tartaruga")
	elif(c==5):	
		print("Animal: Garca")
	elif(c==10):	
		print("Animal: Arara")
	elif(c==20):	
		print("Animal: Mico-leao-dourado")	
	elif(c==50):	
		print("Animal: Onca-pintada")
	elif(c==100):	
		print("Animal: Garoupa")	
else:
	print("Entrada: ", c)
	print("Animal: Invalido")
	