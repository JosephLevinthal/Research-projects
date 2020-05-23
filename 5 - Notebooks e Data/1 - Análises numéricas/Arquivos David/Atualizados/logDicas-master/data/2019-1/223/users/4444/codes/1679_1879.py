extra = float(input('digite o numero de horas extras: '))
faltas=float(input('digite faltas:   '))
print(extra,'extras e',faltas,'de falta')
h = extra - 0.25 * faltas
if(h > 400):
	print('R$',round(500.0, 2))
else:
	print('R$',round(100.0, 2))
				 

