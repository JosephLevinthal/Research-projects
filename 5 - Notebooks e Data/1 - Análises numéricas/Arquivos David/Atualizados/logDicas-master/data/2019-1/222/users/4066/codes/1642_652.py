num1 = int(input('Digite um numero de 3 digitos: '))

dig = num1 // 100

num2 = num1 - dig*100
div = num1 % num2

if (div == 0):
	print('SIM')
	
else:
	print('NAO')