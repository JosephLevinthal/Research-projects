# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
ce = float(input('Digite o consumo de energia: '))
ti = input('Qual o tipo de instalacao? ').upper()
print('Entradas:', ce, 'kWh e tipo', ti)

if (ce>0):
	if (ce<=500 and ti=='R'):
		print('Valor total: R$', round(ce*0.44, 2))
	elif (ce>500 and ti=='R'):
		print('Valor total: R$', round(ce*0.65, 2))
	elif (ce<=1000 and ti=='C'):
		print('Valor total: R$', round(ce*0.55, 2))
	elif (ce>1000 and ti=='C'):
		print('Valor total: R$', round(ce*0.60, 2))
	elif (ce<=5000 and ti=='I'):
		print('Valor total: R$', round(ce*0.55, 2))
	elif (ce>5000 and ti=='I'):
		print('Valor total: R$', round(ce*0.60, 2))
else:
	print('Dados invalidos')