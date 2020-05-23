v = input("Insira: ")
saida = " "
for i in range(len(v)):
	if v[i].upper() != "A":
		saida = saida + v[i]
print(saida)
		