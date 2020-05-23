cidadeA = int(input("Habitantes da cidade A: "))
cidadeB = int(input("Habitantes da cidade B: "))
crescimentoA = float(input("Percentual de crescimento populacional A: "))
crescimentoB = float(input("Percentual de crescimento populacional B: "))

anos = 0

while (cidadeA < cidadeB):
	cidadeA = cidadeA + (cidadeA * (crescimentoA / 100))
	cidadeB = cidadeB + (cidadeB * (crescimentoB / 100))
	anos = anos + 1
	
print (anos)