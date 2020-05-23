ld= int(input("insira o numero sorteado no lancamento do dado 1: "))
ld1= int(input("insira o numero sorteado no lancamento do dado 2: "))
nr= int(input("insira o numero de rodadas: "))
if ((ld and ld1)>=1) and ((ld and ld1)<=6):
	if (ld+ld1==12):
		print("CONSTRICAO")
		print(ld+ld1+1)
	elif (ld+ld1)<5:
		print("POLEN")
		print((ld+ld1+1)*nr)
	else:
		print("FRAQUEZA")
		print(ld*ld1)
else:
	print("Entrada invalida")