s = input()

saida = ""

for i in range(len(s)):
	if s[i].lower() != "a":
		saida = saida + s[i]
print(saida)