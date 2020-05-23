from numpy import*
from numpy.linalg import*

m=array(eval(input("")))

s=m.shape[0]
f=0
d=0
for i in range(s):
	f=min(m[i,:])
	d=d+f
p=d
print(round(p/s,2))