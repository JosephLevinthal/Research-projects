from numpy import*
from math import*

x=float(input("digite: "))
k=int(input("digite: "))
i=0
s=0
while(k>i):
	s=s+(x**(2*i+1)/factorial(2*i+1))
	i=i+1
	
print(round(s,9))
	