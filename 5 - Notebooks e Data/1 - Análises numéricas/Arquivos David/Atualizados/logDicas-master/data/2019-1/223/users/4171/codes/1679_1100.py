valor = int(input("valor da cedula: "))

if valor == 2 or valor == 5 or valor == 10 or valor == 20 or valor == 50 or valor == 100:
	if valor == 2:
		animal = ("Tartaruga")
	elif valor == 5:
		animal = ("Garca")
	elif valor == 10:
		animal = ("Arara")
	elif valor == 20:
		animal = ("Mico-leao-dourado")
	elif valor == 50:
		animal = ("Onca-pintada")
	elif valor == 100:
		animal = ("Garoupa")
	print("Entrada:", valor)
	print("Animal:", animal)
else:
	print("Entrada: ", valor)
	print("Animal: Invalido")