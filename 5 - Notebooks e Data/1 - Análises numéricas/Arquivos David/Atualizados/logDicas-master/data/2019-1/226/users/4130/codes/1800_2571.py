string = input("Digite: ")

saida = ""

for i in range(len(string)):
	if(string[i].lower() != "a"):
		saida = saida + string[i]
print(saida)