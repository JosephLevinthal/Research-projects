from numpy import *
v1=array(eval(input()))
n=size(v1)
mult=1

m=sum(v1)/size(v1)
for i in range(size(v1)):
	a=abs(v1[i]-m)
	mult=mult*a
p=(mult)**(1/n)
print(round(p,3))

