hA = float(input("Numero de habitantes da cidade A: "))
hB = float(input("Numero de habitantes da cidade B: "))
pA = float(input("Taxa de crescimento da cidade A: "))
pB = float(input("Taxa de crescimento da cidade B: "))

t = 0

while(hA < hB):
	creA = hA * (pA / 100)
	creB = hB * (pB / 100)
	hA = hA + creA
	hB = hB + creB
	t = t + 1
print(t)