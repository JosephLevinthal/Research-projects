from math import*
from numpy import*
x=array(eval(input("")))
m=sum(x)/size(x)
b=1
for i in range(size(x)):
	d=abs((x[i]-m))
	b=b*d
f=(b)**(1/size(x))
print(round(f,3))
