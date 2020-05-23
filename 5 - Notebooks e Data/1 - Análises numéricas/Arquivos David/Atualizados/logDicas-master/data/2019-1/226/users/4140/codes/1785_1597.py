from numpy import*
v1=array(eval(input()))
i=0
soma=0
while(i<size(v1)):
	if(v1[i]>80):
		v[i]=v[i]-5
	i=i+1
a=sum(v1)
print(round(a,2))