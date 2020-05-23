
from math import *
k=int(input("digite o numero:"))
i=0
s=1

while	(i<k-1):
	i=i+1
	s=s+1/factorial(i)
print(round(s,8))