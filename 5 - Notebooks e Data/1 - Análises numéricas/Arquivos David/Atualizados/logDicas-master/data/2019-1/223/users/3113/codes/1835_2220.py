from numpy import*
from numpy.linalg import*

m=array(eval(input("")))

s=m.shape[0]
f=0
for i in range(s):
	f=max(m[i,:])
	print(f)