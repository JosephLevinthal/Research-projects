s = input("Insira: ")
saida = ""
for i in range(len(s)):
	if((s[i] == "A") or (s[i] == "a")):
		saida = saida + ""
	else:
		saida = saida + s[i]
print(saida)