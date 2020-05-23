hA = int(input("numero de habitantes de A:"))
hB = int(input("numero de habitantes de B:"))
pA = float(input("crescimento populacional de A:"))
pB = float(input("crescimento populacional de B:"))

percA = pA / 100
percB = pB / 100

ano = 0

while(hA < hB):
	hA = hA + (hA * percA)
	hB = hB + (hB * percB)
	ano = ano + 1
	
print(ano)