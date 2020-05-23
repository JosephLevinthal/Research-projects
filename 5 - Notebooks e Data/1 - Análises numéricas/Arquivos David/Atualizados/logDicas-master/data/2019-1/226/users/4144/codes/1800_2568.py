from numpy import *
n = int(input("nro: "))
for i in range(n):
	x = n*"*" + i*"o" + i*"o" + n*"*"
	n = n -1
	print(x)