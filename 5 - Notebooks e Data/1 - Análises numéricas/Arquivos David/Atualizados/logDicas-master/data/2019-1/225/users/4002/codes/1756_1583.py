s = input("caracteres numericos:")
i = 0
saida = s[0:3]
while(i < len(s) - 3):
	i = i + 3
	saida = saida + "." + str(s[i : i + 3])

print(saida)