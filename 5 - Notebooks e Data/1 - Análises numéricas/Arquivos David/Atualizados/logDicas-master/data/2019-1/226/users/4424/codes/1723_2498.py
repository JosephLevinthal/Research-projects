hA = int(input("escreva: "))
hB = int(input("escreva: "))
pA = float(input("escreva: "))
pB = float(input("escreva: "))

percA=pA/100
percB=pB/100

ano=0

while(hA<hB):
	hA=hA+(hA*percA)
	hB=hB+(hB*percB)
	ano=ano+1
print(ano)