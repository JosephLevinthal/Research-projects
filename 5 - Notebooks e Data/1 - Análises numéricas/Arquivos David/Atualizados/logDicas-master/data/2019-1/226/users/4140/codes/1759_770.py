from numpy import*
v1=zeros(26,dtype=int)
v2=zeros(26,dtype=int)
i=0
j=0
k=0
soma=0
v3=input().lower()
v4=input().lower()
while(i<len(v3)):
	a=ord(v3[i])
	a=a-98
	v1[a]=v1[a]+1
	i=i+1
while(j<len(v4)):
	a=ord(v4[j])
	a=a-98
	v2[a]=v2[a]+1
	j=j+1
v5=v1-v2
print(v5)
while(k<size(v1)):
	if(v1[k]!=v2[k]):
		soma=soma+1
	k=k+1
if(soma!=0):
	print(0)
else:
	print(1)
