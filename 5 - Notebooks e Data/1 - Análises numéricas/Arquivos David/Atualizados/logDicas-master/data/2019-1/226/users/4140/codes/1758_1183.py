from numpy import*
v= array(eval(input()))
i=0
a=0
j=0
k=0
while(i<size(v)):
	if(v[i]>=0):
		a=a+1
	i=i+1
v2=arange(a)
while(j<size(v)):
	if(v[j]>0):
		v2[k]=v[j]
		k=k+1
		
	j=j+1
print(v2)


