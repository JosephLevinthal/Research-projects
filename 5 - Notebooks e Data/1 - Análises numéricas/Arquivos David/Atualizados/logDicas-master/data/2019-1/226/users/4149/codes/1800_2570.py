from numpy import*
from math import*
v=array(eval(input("entre com o vetor:")))

m= sum(v)/size(v)
i=1
n=size(v)
for y in v:
	i=i*abs(y-m)
i=i**(1/n)
print(round(i,3))