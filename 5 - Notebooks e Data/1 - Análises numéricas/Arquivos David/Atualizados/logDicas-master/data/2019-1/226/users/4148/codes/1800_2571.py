strt = input('')

saida = ''

for i in range(len(strt)):
	if strt[i].upper() != 'A':
		saida = saida + strt[i]
print(saida)		