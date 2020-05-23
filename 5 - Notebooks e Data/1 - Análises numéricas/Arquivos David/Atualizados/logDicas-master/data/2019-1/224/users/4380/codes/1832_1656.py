from numpy import *
v=input("")
v=v.upper()
v=v.split(',')
p=0
v2=zeros(5,dtype=int)
k=0
for p in v:
	if(p=="BE"):
		v2[0]=v2[0]+1
	elif(p=="ES"):
		v2[1]=v2[1]+1
	elif(p=="FR"):
		v2[2]=v2[2]+1
	elif(p=="IT"):
		v2[3]=v2[3]+1
	elif(p=="PT"):
		v2[4]=v2[4]+1
	k=k+1
print(max(v2))
print(v2)