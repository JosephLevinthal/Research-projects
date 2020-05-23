from numpy import*
from math import*
a=array(eval(input("vetor: ")))
b=1
for i in range(size(a)):
	b=b * abs(a[i]-(sum(a)/size(a)))
c = (b)**(1/size(a))	
print(round(c,3))