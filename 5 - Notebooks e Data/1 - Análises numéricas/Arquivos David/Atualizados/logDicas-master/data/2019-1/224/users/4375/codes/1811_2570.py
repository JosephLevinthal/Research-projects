from numpy import*
from math import*
x=array(eval(input("digite o vetor: ")))
m=sum(x)/size(x)
s=1
for i in x:
	s=s*abs(i-m)
	d=(s)**(1/size(x))
print(round(d,3))