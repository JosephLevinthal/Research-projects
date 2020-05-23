p = float(input("Digite o percurso em km: "))
c = input("Digite o tipo de carro (A ou B): "). upper()

if(c =="A"):
	x = p / 8
	print(round(x,2))

else:
	y = p / 12
	print(round(y,2))
