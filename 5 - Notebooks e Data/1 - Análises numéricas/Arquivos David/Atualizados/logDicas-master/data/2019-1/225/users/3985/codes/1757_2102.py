from numpy import*

v=array(eval(input()))
i=0
while(i<size(v)):
	if(v[i]%2==1):
		v[i]=0
	i+=1
print(v)