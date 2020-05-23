s = float(input("percuso: "))
car = input("tipo de carro: (A/B)")

if car == "A":
	consumo = s / 8
	print(round(consumo, 2))
if car == "B":
	consumo = s/ 12
	print(round(consumo, 2))