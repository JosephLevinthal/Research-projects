a = float(input('consumo: '))
b = str(input('tipo: '))

print('Entradas:',a, 'kWh e tipo',b)
if (a > 0) and ((b.lower() == 'r')or (b.lower() == 'i') or (b.lower() == 'c')):
	if (b.lower() == 'c') and (a > 1000):
		print('Valor total: R$',round(a*0.60,2))
	elif (b.lower() == 'c') and (a <= 1000):
		print('Valor total: R$',round(a*0.55,2))
	elif (b.lower() == 'r') and (a > 500):
		print('Valor total: R$',round(a*0.65,2))
	elif(b.lower() == 'r') and (a<= 500):
		print('Valor total: R$',round(a*0.44,2))
	elif (b.lower() == 'i') and (a > 5000):
		print('Valor total: R$',round(a*0.60,2))
	elif (b.lower() == 'i') and (a <= 5000):
		print('Valor total: R$',round(a*0.55,2))
	else:
		print('Dados invalidos')
else:
	print('Dados invalidos')
	