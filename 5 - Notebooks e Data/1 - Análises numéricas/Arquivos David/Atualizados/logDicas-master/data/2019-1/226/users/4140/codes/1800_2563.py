from numpy import *
v1=array(eval(input()))

while (size(v1)>1):
	soma=0
	for i in range(size(v1)):
		if(v1[i]>=5 and v1[i]<7):
			soma =soma+1
	print(soma)
	v1=array(eval(input()))
