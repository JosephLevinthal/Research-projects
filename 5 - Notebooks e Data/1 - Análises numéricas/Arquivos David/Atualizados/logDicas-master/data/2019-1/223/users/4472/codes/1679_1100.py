cedula = int(input("Valor da cedula: "))

if (cedula == 2):
	Animal = "Tartaruga"
elif (cedula == 5):
	Animal = "Garça"
elif (cedula == 10):
	Animal = "Arara"
elif (cedula == 20):
	Animal = "Mico-leao-dourado"
elif (cedula == 50):
	Animal = "Onca-pintada"
elif (cedula == 100):
	Animal = "Garoupa"
else:
	Animal = "Invalido"

print ("Entrada: ", cedula)
print ("Animal: ", Animal)