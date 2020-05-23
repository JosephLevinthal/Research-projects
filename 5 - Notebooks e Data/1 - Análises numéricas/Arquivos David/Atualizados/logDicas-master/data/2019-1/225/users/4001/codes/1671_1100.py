# Entradas
X = int(input("Cedula: "))
print("Entrada: ", X)
# Condicoes
if (X == 2):
	print("Animal: Tartaruga")
elif (X == 5):
	print("Animal: Garca")
elif (X == 10):
	print("Animal: Arara")
elif (X == 20):
	print("Animal: Mico-leao-dourado")
elif (X == 50):
	print("Animal: Onca-pintada")
elif (X == 100):
	print("Animal: Garoupa")
elif (X != 2) or (X != 5) or (X != 10) or (X != 20) or (X != 50) or (X != 100):
	print ("Animal: Invalido")
