a = int(input('1. numero '))
b = int(input('2. numero '))

c = a*b
par = c % 2

if (par == 0):
	print(a+b)
	
else:
	print(b - a)