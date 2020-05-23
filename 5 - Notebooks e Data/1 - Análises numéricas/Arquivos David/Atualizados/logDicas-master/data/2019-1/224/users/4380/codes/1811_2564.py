from numpy import *
v1=array(eval(input("time 1: ")))
v2=array(eval(input("time 2: ")))
v=0
i=0
g=0
e=0
d=0
a=zeros(3, dtype=int)
while (i<size(v1)):
	while(size(v1)>g):
		if(v1[i]>v2[g]):
			v=v+1
		elif(v1[i]==v2[g]):
			e=e+1
		else:
			d=d+1
		g=g+1
		i=i+1
a[0]=v
a[1]=e
a[2]=d
print(a)