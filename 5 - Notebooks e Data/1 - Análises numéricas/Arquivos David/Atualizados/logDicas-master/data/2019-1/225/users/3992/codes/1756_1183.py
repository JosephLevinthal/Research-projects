from numpy import * 
v = array(eval(input(":")))
i = 0
n = 0 
while	(i < size(v)):
	if(v[i]<0):
		n = n + 1
	i = i + 1
i=0
k =0
b = arange(size(v)-n)
while	(i < size(v)):
	if(v[i]>=0):
		b[k]=v[i]
		k=k+1
	i = i + 1
print(b)
	
