a = int(input("hab1: "))
b = int(input("hab2: "))
p1 = float(input("pA: "))
p2 = float(input("pB: "))

percA = p1 / 100
percB = p2 / 100

ano = 0

while (a < b):
	a = a + (a * percA)
	b = b + (b * percB)
	ano = ano + 1

print(ano)