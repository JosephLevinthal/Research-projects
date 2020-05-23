from numpy import*
v1=input()
v1= v1.split()
v1="".join(v1)
v1=v1.upper()
i=0
j=-1
soma=0
while(i<len(v1) and abs(j)<=len(v1)):
	if(v1[i])!=v1[j]:
		soma=soma+1
	i=i+1
	j=j-1
print(v1)
if(soma==0):
	print(1)
else:
	print(0)
