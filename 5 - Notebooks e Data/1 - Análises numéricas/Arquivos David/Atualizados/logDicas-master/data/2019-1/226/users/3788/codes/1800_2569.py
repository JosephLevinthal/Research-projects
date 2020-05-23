from numpy import *
from math import *

v=array(eval(input()))

acm=0
for i in range(size(v)):
	acm=acm+v[i]
d=0
media=acm/size(v)
for j in range(size(v)):
	d=d+(v[j]-media)**2

total=sqrt(d/(size(v)-1))
print(round(total,3))

