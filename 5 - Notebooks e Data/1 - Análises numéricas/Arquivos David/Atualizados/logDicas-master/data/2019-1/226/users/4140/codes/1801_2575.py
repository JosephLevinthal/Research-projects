from numpy import*
v1=array(eval(input().upper()))
v2=zeros(3,dtype=int)
for i in range(size(v1)):
	if(v1[i]=="TV"):
		v2[0]=v2[0]+1
	if(v1[i]=="NETFLIX"):
		v2[1]=v2[1]+1
	if(v1[i]=="YOUTUBE"):
		v2[2]=v2[2]+1
print(v2)
	