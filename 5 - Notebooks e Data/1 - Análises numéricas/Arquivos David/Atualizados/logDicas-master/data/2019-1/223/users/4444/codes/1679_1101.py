faixa=float(input('qual o consumo de energia: '))
tipo=input('tipo de instalacao R, I ou C:  ')
tipo=tipo.upper()
if(faixa <=0):
	
	print("Entradas: ", faixa, "kWh e tipo", tipo)
	print('Dados invalidos')
elif(tipo != 'R') and (tipo != 'I') and (tipo != 'C'):
	print("Entradas:", faixa, "kWh e tipo", tipo)
	print('Dados invalidos')
elif(tipo == 'R') and (faixa <= 500):
	print("Entradas: ", faixa,"kWh e tipo", tipo)
	print('Valor total: R$',round(faixa * 0.44, 2))
elif(tipo == 'R') and (faixa > 500):
	print("Entradas:", faixa, "kWh e tipo", tipo)
	print('Valor total: R$',round(faixa * 0.65, 2))
	
elif(tipo == 'C') and (faixa <= 1000):
	print("Entradas:", faixa, "kWh e tipo", tipo)
	print('Valor total: R$',round(faixa * 0.55, 2))
elif(tipo == 'C') and (faixa > 1000):
	print("Entradas:", faixa, "kWh e tipo", tipo)
	print('Valor total: R$',round(faixa * 0.60, 2))
	
#industrial <=5000
elif(tipo == 'I') and (faixa <= 5000):
	print('Entradas:', faixa, 'kWh e tipo', tipo)
	print('Valor total: R$',round(faixa * 0.55, 2))
	
elif(tipo == 'I') and (faixa > 5000):
	print("Entradas:", faixa, 'kWh e tipo', tipo)
	print('Valor total: R$',round(faixa * 0.60, 2))




	
