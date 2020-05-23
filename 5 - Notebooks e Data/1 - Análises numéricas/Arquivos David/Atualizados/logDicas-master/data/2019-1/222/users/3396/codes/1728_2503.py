

n = int(input("Digite n :"))
pii = 0
cont = 1
c = 1
sinal = 1
while cont <= n :
	termo = 4 / c
	c = c + 2
	pii = pii + (termo * sinal)
	cont = cont + 1
	sinal = sinal * (-1)
print(round(pii,8))