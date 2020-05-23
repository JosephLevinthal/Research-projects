a = int(input('idade: '))
IMC = float(input('IMC: '))

print('Entradas: ',a,'anos e IMC',IMC)

if ((a<=0) or (a>130)) and (IMC<=0):
	print('Dados invalidos')
elif (a<45) and (IMC<22.0):
	print('Risco: Baixo')
elif (a<45) and (IMC>=22.0):
	print('Risco: Medio')
elif (a>=45) and (IMC<22.0):
	print('Risco: Medio')
elif (a>=45) and (IMC>=22.0):
	print('Risco: Alto')