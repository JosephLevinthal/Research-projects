escala = input("Escala: ")
temperatura = float(input("Valor da temperatura: "))

if (escala == "C"):
	conversao = (9*temperatura +160)/5
	print(conversao)
else:
	conversao = 5/9*(temperatura-32)
	print(conversao)