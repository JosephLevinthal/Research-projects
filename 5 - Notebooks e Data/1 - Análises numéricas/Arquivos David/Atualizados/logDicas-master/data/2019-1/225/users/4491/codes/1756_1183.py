from numpy import*
a= array(eval(input()))
i=0
j=0
k=0
while(k<size(a)):
	if(a[k]>0):
		i=i+1
	k=k+1
k=0
v=arange(i)
while(k<size(a)):
	if(a[k]>0):
		v[j]=a[k]
		j=j+1
	k=k+1
print(v)


