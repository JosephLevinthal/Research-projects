pA = int(input("Populacao da cidade A: "))
pB = int(input("Populacao da cidade B: "))
txA = float(input("Taxa de crescimento da cidade A: "))
txB = float(input("Taxa de crescimento da cidade B: "))
qtdAnos = 0
while pA < pB :
	pA = pA + pA*txA/100
	pB = pB + pB*txB/100
	qtdAnos = qtdAnos + 1
print(qtdAnos)