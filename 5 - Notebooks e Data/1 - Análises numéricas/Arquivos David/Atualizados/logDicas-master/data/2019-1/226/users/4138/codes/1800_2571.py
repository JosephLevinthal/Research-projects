n = input("insira a string:")

saida = ""

for i in range(len(n)):
	if(n[i].upper() != "A"):
		saida = saida + n[i]
print(saida)
		