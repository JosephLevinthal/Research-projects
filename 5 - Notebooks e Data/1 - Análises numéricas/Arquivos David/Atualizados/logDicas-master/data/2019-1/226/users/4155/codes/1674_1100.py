x = int(input("valor da cedula: "))
print("Entrada:", x)
if((x == 2) or (x == 5) or (x == 10) or (x == 20) or (x == 50) or (x == 100)):
	if(x == 2):
		print("Animal: Tartaruga")
	else:
		if(x == 5):
			print("Animal: Garca")
		else:
			if(x == 10):
				print("Animal: Arara")
			else:
				if(x == 20):
					print("Animal: Mico-leao-dourado")
				else:
					if(x == 50):
						print("Animal: Onca-pintada")
					else:
						if(x == 100):
							print("Animal: Garoupa")
						else:
							print("Animal: Invalido")
else:
	print("Animal: Invalido")
	
	



