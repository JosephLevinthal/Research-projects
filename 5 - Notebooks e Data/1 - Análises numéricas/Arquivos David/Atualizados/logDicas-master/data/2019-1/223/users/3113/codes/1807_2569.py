from math import*
from numpy import*
x=array(eval(input("")))
m=sum(x)/size(x)
b=0
for i in range(size(x)):
	d=(x[i]-m)**2
	b=b+d
f=(b/(size(x)-1))**0.5
print(round(f,3))
