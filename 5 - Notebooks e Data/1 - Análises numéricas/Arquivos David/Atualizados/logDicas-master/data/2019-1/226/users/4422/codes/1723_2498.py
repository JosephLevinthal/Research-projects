a = int(input("hab. A: "))
b = int(input("hab. B: "))
pa = float(input("c. p. A: "))
pb = float(input("c.p.B: "))

percA = pa/100
percB = pb/100

ano = 0

while(a < b):
	a = a + (a * percA)
	b = b + (b * percB)
	ano = ano + 1
	
print(ano)