from numpy import *
v=array(eval(input("Digite vetor: ")))*1.0

v2 = arange(size(v),dtype=float)

i =0 

while(i< size(v)):
	if(v[i]>80.0):
		v2[i]= v[i] - 5.0
	else:
		v2[i]=v[i]
	i+=1

print(round(sum(v2),2))
