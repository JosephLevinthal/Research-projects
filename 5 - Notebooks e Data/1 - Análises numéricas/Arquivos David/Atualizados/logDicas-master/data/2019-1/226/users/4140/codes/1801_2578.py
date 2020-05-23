from numpy import*
v1=array(eval(input()))
a=0
j=0
k=0
b=0
for i in range(size(v1)):
	if(v1[i]%2==0):
		a=a+1
	else:
		b=b+1
v2=zeros(a,dtype=int)
while(j<size(v1)):
	if(v1[j]%2==0):
		v2[k]=v1[j]
		k=k+1
	j=j+1
print(v2)