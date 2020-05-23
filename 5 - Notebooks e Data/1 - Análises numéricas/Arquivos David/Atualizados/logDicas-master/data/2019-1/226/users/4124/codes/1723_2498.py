numA = int(input("Numero de habitantes da cidade A:"))
numB = int(input("Numero de habitantes da cidade B:"))
taxA = float(input("Percentual de crescimento de A:"))
taxB = float(input("Percentual de crescimento de b:"))
ano = 0
while(numA < numB):
	ano = ano + 1
	crea = numA * (taxA / 100)
	creb = numB * (taxB / 100)
	numA = numA + crea
	numB = numB + creb
print(ano)
	