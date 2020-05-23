na = int(input("Numero de habitantes de A: "))
nb = int(input("Numero de habitantes de B: "))
pa = float(input("percentual de crescimento de A: "))
pb = float(input("percentual de crescimento de b: "))

cna = na + ((na * pa) / 100)
cnb = nb + ((nb * pb) / 100)
ct = 1
while(cna < cnb):
	cna = cna + ((cna * pa) / 100)
	cnb = cnb + ((cnb * pb) /100)
	ct = ct+1
print(ct)