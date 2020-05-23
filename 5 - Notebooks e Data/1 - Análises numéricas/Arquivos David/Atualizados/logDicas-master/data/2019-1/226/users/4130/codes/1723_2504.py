c = int(input("Quantidade inicial de copias: "))
l = int(input("Quantidade inicial de leucocitos: "))
pv = int(input("Percentual do virus: ")) / 100
pl = int(input("Percentual de leucocito: ")) / 100

d = 0

while(l < (2 * c)):
	c = c + pv * c
	l = l + pl * l
	d = d + 1
print(d)