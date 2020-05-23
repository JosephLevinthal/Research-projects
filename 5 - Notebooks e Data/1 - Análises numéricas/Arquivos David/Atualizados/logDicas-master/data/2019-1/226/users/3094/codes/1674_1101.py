# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
ce = float(input("consumo de energia: "))
tipo = input("tipo de instalacao: ").upper()
print('Entradas: ', ce, ' kWh ' 'e tipo ', tipo )

r1 = round(ce*(0.44),2)
r = round(ce*(0.65), 2)
c1 = round(ce*(0.55), 2)
c = round(ce*(0.60),2)
i1 = round(ce*(0.55),2)
i= round(ce*(0.60),2)

if(ce>0):
	if(tipo =='R') and (ce<=500):
		print('Valor total: ', 'R$', r1)
	elif (tipo =='R') and (ce > 500):
		print('Valor total: ', 'R$', r)
	elif(tipo=='C') and (ce <= 1000):
		print('Valor total: ', 'R$', c1)
	elif(tipo=='C')and(ce >1000):
		print('Valor total: ', 'R$', c)
	elif(tipo=='I') and(ce<=5000):
		print('Valor total: ', 'R$', i1)
	elif(tipo=='I')and(ce>5000):
		print('Valor total: ', 'R$', i)
	else:
		print('Dados invalidos')
	
	
	
	