from numpy import *
fra = input("Sequencia polindromo: ")
frase = fra.replace(" ","")

print(frase.upper())
cont = 0
cont2 = -1
while cont < size(frase)/2:
	if frase[cont] != frase[cont2]:
		y = "erro"
	else:
		y = "certo"
	cont = cont + 1
	cont2 = cont2 - 1
if y == "erro":
	print(0)
elif y == "certo":
	print(1)