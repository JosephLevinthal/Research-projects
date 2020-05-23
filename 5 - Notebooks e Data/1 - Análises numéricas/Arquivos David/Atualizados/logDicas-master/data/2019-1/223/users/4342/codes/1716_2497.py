saldo=float(input("valor inicial:"))
tempo=int(input("quantidade de anos:"))
juros=4
t=0
while(t<(1*12)):
	saldo= saldo + (saldo*juros)/100
	t=t+1
	while(t<(2*12)):
	saldo= saldo + (saldo*juros)/100
	t=t+1
print(round(saldo, 2))