a = input("digite")

saida = ""

for i in range(len(a)):
	if a[i].lower() != 'a' :
		saida = saida + a[i]
print(saida)