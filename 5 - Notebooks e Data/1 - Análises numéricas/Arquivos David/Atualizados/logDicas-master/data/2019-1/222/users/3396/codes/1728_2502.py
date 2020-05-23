

n = int(input("Digite n :"))
pii = 0
cont = 1
c = 1
sinal = 1

while cont <= n:
	termo =  1 / (c*(3**(cont - 1)))
	c = c + 2
	pii = pii + (termo * sinal)
	cont = cont + 1
	sinal = sinal * (-1)
print(round(((12**0.5)*pii),8))
