PO = int(input('quantas pecas de ouro possui: '))
a = str(input('nome da armadura: ')).upper()
d = int(input('numero de 1 a 8: '))
I = 200
M = 50
P = 100
if (a == 'INTEIRA') or (a == 'MALHA') or (a == 'PLACA'):
	if (a == 'INTEIRA'):
		if PO>=I:
			print(30*d-20)
		else:
			print('PO insuficiente')
	elif a == 'MALHA':
		if PO>=M:
			print(15*d-1)
		else:
			print('PO insuficiente')
	elif a == 'PLACA':
		if PO>=P:
			print(20*d-18)
		else:
			print('PO insuficiente')
else:
	print('Entrada invalida')