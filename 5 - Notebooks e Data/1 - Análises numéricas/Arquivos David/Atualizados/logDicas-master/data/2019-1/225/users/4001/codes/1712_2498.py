nA = int(input("Cidade A: "))
nB = int(input("Cidade B: "))
pA = float(input("pA da cidade: "))
pB = float(input("pB da cidade: "))
t = 0 

while (nA < nB):
	nA = nA + nA * pA/100
	t = t + 1
	nB = nB + nB * pB/100
print(t)

 
	