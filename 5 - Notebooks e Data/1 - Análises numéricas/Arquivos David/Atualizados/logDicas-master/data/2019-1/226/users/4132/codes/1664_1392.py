consumo = float(input("Digite o consumo: "))


if( consumo < 10 ):
	consumo = 30 + 3 * consumo
else:
	consumo = 30 + 3.5 *consumo
	
print(round(consumo,2))