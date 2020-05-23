peso = float(input("Digite o peso: "))
if(peso <= 4999.9):
	total = 0.05 * peso
else:
	total = ((0.04 * peso) + 60)
print(round(total,2))