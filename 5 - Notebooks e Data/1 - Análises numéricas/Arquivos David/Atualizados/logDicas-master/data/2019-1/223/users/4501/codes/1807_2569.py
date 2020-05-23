from numpy import*
from math import*
a=array(eval(input("vetor: ")))
d=0
for i in range(size(a)):
	d=d+(a[i]-(sum(a)/size(a)))**2
d=sqrt(d/(size(a)-1))	
print(round(d, 3))
	