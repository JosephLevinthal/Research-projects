from numpy import *

n = int(input("insira o numero:"))

for i in range(n):
	print((n-i)*"*" + i* "o" + i*"o" + (n-i)*"*")
	

	