from numpy import *
v1=array(eval(input()))
n=size(v1)
v2=zeros(n,dtype=int)
i=0
while(i<n):
	if(v1[i]%2==0):
		v2[i]=v1[i]
	else:
		v2[i]=0
	i=i+1
print(v2)