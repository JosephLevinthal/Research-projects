from numpy import*
from math import*
x= array(eval(input("seu vetor")))
m= sum(x)/size(x)
p=1
for i in range(size(x)):
	p= p*(abs(x[i]-m))
p=(p)**(1/size(x))
print(round(p,3))