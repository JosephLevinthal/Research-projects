ha = int(input("h cidade A: "))
hb = int(input("h cidade B: "))
cpA = float(input("cp cidadade A: "))
cpB = float(input("cp cidadade B: "))

perA = cpA/100
perB = cpB/100

ano = 0

while (ha<hb):
	ha = ha + (ha*perA)
	hb = hb + (hb*perB)
	ano = ano + 1
print(ano)
