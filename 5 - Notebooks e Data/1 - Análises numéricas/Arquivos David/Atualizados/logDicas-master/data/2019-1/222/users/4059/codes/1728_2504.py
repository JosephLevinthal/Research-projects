v = int(input("Quantidade inicial copias: "))
l = int(input("Quantidade inicial leucocitos: "))

pv = float(input("Percentual do virus: "))
pl = float(input("Percentual dos leucocitos: "))
dias = 0

while (l < 2*v):
	v = v + v*pv/100
	l = l + l*pl/100
	dias = dias + 1
print(dias)