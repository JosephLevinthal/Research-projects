hA = int(input("Digite aqui o numero de habitantes a cidade A: "))
hB = int(input("Digite aqui o numero de habitantes a cidade B: "))
pA = float(input("Digite aqui o percentual de crescimento populacional da cidade A: "))
pB = float(input("Digite aqui o percentual de crescimento populacional da cidade B: "))
percA = pA / 100
percB = pB / 100
ano = 0
while (hA < hB):
	hA = hA + (hA * percA)
	hB = hB + (hB * percB)
	ano = ano + 1
print(ano)
	