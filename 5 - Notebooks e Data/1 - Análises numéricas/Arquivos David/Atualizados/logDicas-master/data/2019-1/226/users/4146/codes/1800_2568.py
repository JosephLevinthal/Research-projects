from numpy import *
k = int(input("Numero de entrada: "))
j = k
t = 0

for x in range(k):
	v = j*"*" + 2*t*"o" + j*"*"
	j = j - 1
	print(v)
	t = t + 1