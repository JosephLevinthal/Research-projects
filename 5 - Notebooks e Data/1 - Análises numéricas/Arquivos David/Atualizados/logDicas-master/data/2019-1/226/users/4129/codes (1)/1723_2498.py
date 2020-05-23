nA = int(input("Numero de habitantes da cidade A:"))
nB = int(input("Numero de habitantes da cidade B:"))
pA = float(input("Percentual de crescimento populacional da cidade A:"))
pB = float(input("Percentual de crescimento populacional da cidade B:"))

pA = pA/100
pB = pB/100

ano = 0

while(nA < nB):
	nA = nA + nA*pA
	nB = nB + nB*pB
	ano = ano + 1
print(ano)