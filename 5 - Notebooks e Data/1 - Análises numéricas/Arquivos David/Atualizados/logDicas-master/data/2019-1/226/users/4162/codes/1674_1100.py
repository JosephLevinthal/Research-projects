vc= int(input("insira o valor da cedula: "))
print("Entrada:",vc)
if (vc==2) or (vc==5) or (vc==10) or (vc==20) or (vc==50) or (vc==100):
	if (vc==2):
		print("Animal: Tartaruga")
	elif(vc==5):
		print("Animal: Garca")
	elif(vc==10):
		print("Animal: Arara")
	elif(vc==20):
		print("Animal: Mico-leao-dourado")
	elif(vc==50):
		print("Animal: Onca-pintada")
	elif(vc==100):
		print("Animal: Garoupa")
else:
	print("Animal: Invalido")