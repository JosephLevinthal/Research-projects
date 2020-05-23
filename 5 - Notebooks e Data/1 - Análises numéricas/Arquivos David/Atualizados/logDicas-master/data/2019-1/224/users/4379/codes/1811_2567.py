from numpy import *
n=int(input("digite o numero: "))
for i in range(n):
	cpo = "*"*(n-i)
	print(cpo)
for j in range(n):
	cpi="*"*(j+1)
	print(cpi)