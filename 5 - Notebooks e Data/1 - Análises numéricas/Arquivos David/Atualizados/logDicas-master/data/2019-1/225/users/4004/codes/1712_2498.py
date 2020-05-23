hA = int(input("Numero de habitantes de uma cidade A: "))
hB = int(input("Numero de habitantes de uma cidade B: "))
pA = float(input("Percentual de crescimento populacional da cidade A: "))
pB = float(input("Percentual de crescimento populacional da cidade B: "))

t = 0

while (hA <= hB):
	hA = hA + (hA * (pA / 100))
	hB = hB + (hB * (pB / 100))
	t = t + 1
print(t)