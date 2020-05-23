from numpy import*
from math import*
x=array(eval(input("x: ")))
c=sum(x)/size(x)
d=0
for i in x:
	d=d+(i-c)**2
	v=sqrt(d/(size(x)-1))

print(round(v,3))
	