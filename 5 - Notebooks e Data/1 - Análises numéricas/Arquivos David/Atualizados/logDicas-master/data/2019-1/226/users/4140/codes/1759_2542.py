from numpy import *
v1=array(eval(input()))
v2=array(eval(input()))
i=0
soma=0
while(i<size(v1)):
	soma=soma-v2[i]
	if(soma<=75):
		soma=soma+v1[i]
	i=i+1
print(soma)