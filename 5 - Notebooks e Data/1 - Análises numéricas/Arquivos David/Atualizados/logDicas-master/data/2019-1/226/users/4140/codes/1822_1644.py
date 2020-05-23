from numpy import*
soma=0
v1=array(eval(input()))
k=0
for i in range(size(v1)):
	if(v1[i]<5):
		soma=soma+1
v2=zeros(soma,dtype=int)
for j in range(size(v1)):
	if(v1[j]<5):
		v2[k]=j
		k=k+1
print(soma)
print(v2)