escala = input("digite escala: ")
valor = float(input("digite temperatura: "))

if(escala != "F"):
	graus = (1.8*valor)+32
else:
	if(escala == "F"):
		graus = (valor-32)/1.8
	else:
		graus = 0
		print("Valor inválido!")
		
	
print(str(round(graus, 2)))