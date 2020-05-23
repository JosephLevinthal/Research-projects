h = float(input("Digite aqui a quantidade de horas aulas do professor: "))
if(h <= 20):
	total = 50 * h
else:
	total = ((h - (h - 20)) * 50) + (70 * (h - 20))
print(round(total, 2))