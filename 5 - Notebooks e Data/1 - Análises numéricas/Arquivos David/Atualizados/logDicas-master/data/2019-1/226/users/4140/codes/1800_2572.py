from numpy import *
v1=array(eval(input()))
par=0
impar=0
j=0
k=0
for i in range(size(v1)):
	if(v1[i]%2==0):
		par=par+1
	else:
		impar=impar+1
v2=zeros(impar,dtype=int)
while(j<size(v1)):
	if(v1[j]%2!=0):
		v2[k]=v1[j]
		k=k+1
	j=j+1
print((v2))