n = input("")

cont = 0
saida = n[0:3]
while cont < len(n) - 3:
	cont = cont + 3
	saida = saida + "." + str(n[cont : cont + 3])

print(saida)