from numpy import*
v1=array(eval(input()))
v2=zeros(6,dtype=int)
for i in range(size(v1)):
	if(v1[i]==2):
		v2[0]=v2[0]+1
	elif(v1[i]==3):
		v2[1]=v2[1]+1
	elif(v1[i]==4):
		v2[2]=v2[2]+1
	elif(v1[i]==5):
		v2[3]=v2[3]+1
	elif(v1[i]==6):
		v2[4]=v2[4]+1
	elif(v1[i]==7):
		v2[5]=v2[5]+1
a=sum(v2)
v2=(v2*100)/a
for j in range(size(v2)):
	v2[j]=round(v2[j],1)
print(v2)