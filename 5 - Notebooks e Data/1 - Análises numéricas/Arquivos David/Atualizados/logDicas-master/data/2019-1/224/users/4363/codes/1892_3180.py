from numpy import *
a= array(eval(input()))
b = zeros(4,dtype=int)
for i in range(size(a)):
	if(a[i]==1):
		b[0]=b[0]+1
	if(a[i]==2):
		b[1]=b[1]+1
	if(a[i]==3):
		b[2]=b[2]+1
	if(a[i]==4):
		b[3]=b[3]+1
print(b)