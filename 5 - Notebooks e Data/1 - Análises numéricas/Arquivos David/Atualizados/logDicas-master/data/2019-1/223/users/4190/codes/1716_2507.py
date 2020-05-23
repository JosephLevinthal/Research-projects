qi = int(input('qi: '))
pc = float(input('pc: '))

c = 0
while (0<qi<8000):
	crescimento = qi*pc/100
	qi = qi + crescimento
	re = int(input('Re: '))
	qi = qi - re
	c = c+1
if (qi<=0):
	print('ZERO')
else:
	print('MAXIMO')
print(c)