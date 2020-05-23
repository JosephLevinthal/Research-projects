vir = int(input("quantos virus: "))
leu = int(input("quantos leucocitos: "))
pv = (int(input("Percentual de multiplicacao diaria do virus: ")))/100
pl = (int(input("Percentual de multiplicacao diaria dos leucocitos: ")))/100
k = 0
while((leu*2)<vir):
	vir =vir + vir*pv
	leu =leu + leu*pl
	print(vir , leu)
	k = k+1
print(k)
	