from numpy import *
v1=array(eval(input()))
i=0
while(i<size(v1)):
	v1[i]=v1[i]**0.5
	i=i+1
s=(sum(v1)/size(v1))**2
print(round(s,2))