from numpy import *
from numpy.linalg import *
c = array(eval(input("h: ")))
d = shape(c)[0]
tt = zeros(d,dtype=int)
for i in range(d):
	tt[i]=sum(c[i,:])
	
print(tt)