var = int(input("Digite o valor da cedula: "))

if (var == 2):
	txt = "Tartaruga"
elif (var == 5):
	txt = "Garca"
elif (var == 10):
	txt = "Arara"
elif (var == 20):
	txt = "Mico-leao-dourado"
elif (var == 50):
	txt = "Onca-pintada"
elif (var == 100):
	txt = "Garoupa"
else:
	txt = "Invalido"

print("Entrada: ", var)
print("Animal: ", txt)
