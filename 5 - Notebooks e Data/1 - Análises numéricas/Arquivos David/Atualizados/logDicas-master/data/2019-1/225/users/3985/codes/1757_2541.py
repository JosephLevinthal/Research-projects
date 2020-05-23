from numpy import*
from math import*

p=array(eval(input()))
q=array(eval(input()))
x=0
s=0
while(x<size(p)):
	s+= (p[x]-q[x])**2
	x+=1
f=sqrt(s)
print(round(f,4))