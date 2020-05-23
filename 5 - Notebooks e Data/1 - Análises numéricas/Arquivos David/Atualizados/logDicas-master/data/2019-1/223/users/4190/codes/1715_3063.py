po = int(input('Quantidade de pecas de ouro: '))
no = input('Nome da armadura: ').upper()
d = int(input('Fator de destreza: '))

if (d>0 or d<8):
	if (po>=200 and no=='INTEIRA'):
		print(30*d-20)
	elif (po>=50 and no=='MALHA'):
		print(15*d-1)
	elif (po>=100 and no=='PLACA'):
		print(20*d-18)
	else:
		print('PO insuficiente')
else:
	print('Entrada invalida')
	