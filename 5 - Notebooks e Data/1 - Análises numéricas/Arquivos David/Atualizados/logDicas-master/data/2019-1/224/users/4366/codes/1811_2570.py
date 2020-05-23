from numpy import*
from math import*
x=array(eval(input("digite um vetor: ")))
m=sum(x)/size(x)
s=1
for i in x:
	s=s*abs(i-m)
	p=(s)**(1/(size(x)))
print(round(p,3))