from numpy import*
from math import*
x=array(eval(input("digite um vetor: ")))
m=sum(x)/size(x)
s=0
for i in x:
	s=s+(i-m)**2
	d=sqrt(s/(size(x)-1))
print(round(d, 3))