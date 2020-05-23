tg = int(input("Numero de termos: "))
cont = 0
soma = 0 
sinal = 4
n1 = 2
n2 = 3
n3 = 4
p = 3
if ( tg == 1 ):
	print (p)
else:
	while ( cont > tg):
		p = p + (sinal/(n1 * n2 * n3))
		sinal = - sinal
		n1 = n1 + 2
		n2 = n2 + 2
		n3 = n3 + 2
		cont = cont + 1

print(round(soma, 8))