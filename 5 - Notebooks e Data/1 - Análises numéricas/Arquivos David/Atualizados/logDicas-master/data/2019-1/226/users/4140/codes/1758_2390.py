from numpy import*
v1=array(eval(input()))
v2=array(eval(input()))
i=0
r1=0
while(i<size(v1)):
	r=v1[i]/v2[i]
	if(r>r1):
		r1=r
		mes=i+1
	i=i+1
print(mes)
	