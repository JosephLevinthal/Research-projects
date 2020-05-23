from numpy import*
n=int(input())
v=zeros(n,dtype=int)
i=2
v[1]=1
while(i<n):
	v[i]=(v[i-1]+v[i-2])
	i=i+1
print(v)