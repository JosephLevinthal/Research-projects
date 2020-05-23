from numpy import *
v1=array(eval(input()))
v2=array(eval(input()))
n=int(input())
v3=zeros(3,dtype=int)
for i in range(size(v2)):
	if(v1[i]>5 and (v2[i]*100)/n >=75 ):
		v3[0]=v3[0]+1
	elif(v1[i]>=5 and (v2[i]*100)/n <75 ):
		v3[2]=v3[2]+1
	elif(v1[i]<5):
		v3[1]=v3[1]+1
print(v3)
