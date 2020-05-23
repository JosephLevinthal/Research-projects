km = float (input("Digite quantos km foram percorridos:"))
car = input("Digite qaul o tipo do carro? (A / B)  ")
if (car == "A"):
	consumo = (km/8)
else:
	consumo = (km/12)
print (round (consumo,2))	