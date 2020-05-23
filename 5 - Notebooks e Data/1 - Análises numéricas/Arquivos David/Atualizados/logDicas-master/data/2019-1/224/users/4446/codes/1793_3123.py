from numpy import *
v=array(eval(input("digite o vetor: ")))
n=size(v)
i=0
s=0

while(i<size(v)):
	k=v[i]**-1
	s=s+k
	i=i+1
	
m=(s/n)**-1
print(round(m, 2))
	