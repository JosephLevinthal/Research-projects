escala = input("Escala em que a temperatura está representada: ")
valor = float(input("Valor da temperatura: "))

if((escala == "c") or (escala == "C") or (escala == "f") or (escala == "F")):
	if((escala == "c") or (escala == "C")):
		f = ((9 / 5) * (valor)) + 32
		print(round(f, 2))
	else:
		c = (5 / 9) * (valor - 32)
		print(round(c, 2))
else:
	print("Digite uma escala valida")