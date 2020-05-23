x = int(input('Insira sua idade: '))
y = float(input('Insira seu IMC: '))
print('Entradas:',x, 'anos e IMC',y)

if ((x<=0) or (x>130) or (y==0)):
	print('Dados invalidos')
elif (x<45 and y<22):
	print('Risco: Baixo')
elif (x>=45 and y<22):
	print('Risco: Medio')
elif (x<45 and y>=22):
	print('Risco: Medio')
elif (x>=45 and y>=22):
	print('Risco: Alto')
else:
	print('Dados invalidos')