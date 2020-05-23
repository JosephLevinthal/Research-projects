virus = int(input())
leu = int(input())
perc1 = int(input())
perc2 = int(input())
c1 = perc1/100
c2 = perc2/100
dias = 0
while leu <= 2*virus:
	acr = virus * c1
	virus = virus + acr
	acr2 = leu * c2
	leu = leu + acr2
	dias += 1
print(dias)
	