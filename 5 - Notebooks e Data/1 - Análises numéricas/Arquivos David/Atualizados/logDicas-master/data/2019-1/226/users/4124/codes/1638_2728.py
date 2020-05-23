perc = float(input("Quilometros da viagem: "))
car = input("Tipo de carro(A/B): ").upper()
if(car == "A"):
	total = perc / 8
else:
	total = perc / 12
print(round(total,2))