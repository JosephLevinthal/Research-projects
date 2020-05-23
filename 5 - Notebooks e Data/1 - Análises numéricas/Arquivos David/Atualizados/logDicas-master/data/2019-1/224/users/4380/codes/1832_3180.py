from numpy import *
v=array(eval(input("dengue: ")))
i=0
v2=zeros(4,dtype=int)
k=0
for i in range(size(v)):
	if(v[i]==1):
		v2[0]=v2[0]+1
	elif(v[i]==2):
		v2[1]=v2[1]+1
	elif(v[i]==3):
		v2[2]=v2[2]+1
	elif(v[i]==4):
		v2[3]=v2[3]+1
	k=k+1
print(v2)