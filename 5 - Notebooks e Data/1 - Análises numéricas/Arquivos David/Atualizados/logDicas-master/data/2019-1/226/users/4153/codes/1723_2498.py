hA = float(input("Insira a qtd de habitantes da cidade A: "))
hB = float(input("Insira a qtd de habitantes da cidade B: "))
pA = float(input("Insira a taxa de crescimento: "))
pB = float(input("Insira a taxa de crescimento: "))
t = 0
while (hA < hB):
	a = (hA *pA)/100
	hA = hA + a
	b = (hB *pB)/100
	hB = b + hB
	t = t + 1
print(t)