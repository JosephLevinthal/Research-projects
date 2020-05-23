from numpy import*
v= array(eval(input()))
i=0
j=0
while(i<size(v)):
	if(v[i]==max(v)):
		j=j+i
	i=i+1
print(j)