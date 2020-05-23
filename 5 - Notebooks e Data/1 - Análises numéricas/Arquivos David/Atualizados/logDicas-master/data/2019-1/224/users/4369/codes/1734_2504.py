qic = int(input("Digite a quantidade inicial de copia: "))
qil = int(input("Digite a quantidade incial de leucocitos: "))
pv = float(input("Percentual diaria de virus: "))
pl = float(input("Percentual diaria de leucocitos: "))
pv = pv/100
pl = pl/100
dpc = 0
v = qic
l = qil
while l < 2 * v:
	v = v + v * pv
	l = l + l * pl
	dpc = dpc + 1
print(dpc)

