from numpy import*
from math import*
v= array(eval(input("x: ")))
m=sum(v)/size(v)
a=0
for x in v:
	a=a+(x-m)**2
a=sqrt(a/(size(v)-1))
print(round(a, 3))