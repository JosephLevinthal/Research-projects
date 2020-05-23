from numpy import*
from numpy.linalg import*

a=array(eval(input()))
n=shape(a)[0]

for i in range(n):
	print(max(a[i,:]))