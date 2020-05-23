from numpy import *
n=int(input("digite o numero: "))
s=0
for i in range(1, n+1):
	s=1/i+s
print(round(s, 2))