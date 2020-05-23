n= int(input("insira um numero natural maior que 2: "))
from numpy import*
a=zeros(n,dtype=int)
i=0
j=-2
k=-1
while i!= size(a):
	a[i]=a[j]+a[k]
	a[1]=1
	i=1+i
	j=j+1
	k=k+1
print(a)
