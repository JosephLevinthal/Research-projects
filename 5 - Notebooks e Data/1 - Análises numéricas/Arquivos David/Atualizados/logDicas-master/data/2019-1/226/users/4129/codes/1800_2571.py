s = input("Escreva:")

saida = ""

for i in range(len(s)):
	if(s[i].upper() != "A"):
		saida = saida + s[i]
print(saida)