from numpy import*
a=float(input("a:"))
v=float(input("v:"))
n=int(input("n:"))
i=0
l1=arange(n)
l2=zeros(n,dtype=float)
while(i<n):
	l2[i]=(a*l1[i]**2)/2+v*l1[i]
	i=i+1
print(l2)
