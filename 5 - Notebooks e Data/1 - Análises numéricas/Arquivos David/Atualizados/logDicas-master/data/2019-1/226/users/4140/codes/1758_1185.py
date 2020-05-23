from numpy import *
v1=array(eval(input()))
i=0
s=0
while(i<size(v1)):
	if(v1[i]>99):
		s=s+1
		print(i)
	i=i+1
print(s)