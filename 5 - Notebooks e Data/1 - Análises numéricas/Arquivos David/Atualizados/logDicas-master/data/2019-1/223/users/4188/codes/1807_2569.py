from numpy import *
from math import *
a=array(eval(input("vetor: ")))
b = 0
for i in range(size(a)):
	b = b + (a[i]-(sum(a)/size(a)))**2
b=sqrt(b/(size(a)-1))
	
print(round(b,3))