anos = 0
qi = float(input('Quantidade Inicial: '))
pe = float(input('Percentual de crescimento: '))
re = float(input('Quantidade retiradas ao ano: '))

while (0<qi<12000):
	crescimento = qi*pe/100
	qi += crescimento
	qi -= re
	anos += 1
	
if(qi<=0):
	print('EXTINCAO')
else:
	print('LIMITE')
	
print(anos)