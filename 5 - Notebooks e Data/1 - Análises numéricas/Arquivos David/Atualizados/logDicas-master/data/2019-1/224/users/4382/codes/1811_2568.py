from numpy import *
n = int(input('digite a quantidade de asteristicos: '))
for i in range(n):
	print('*'*n + 'o'*(i*2) + '*'*n)
	n = n - 1