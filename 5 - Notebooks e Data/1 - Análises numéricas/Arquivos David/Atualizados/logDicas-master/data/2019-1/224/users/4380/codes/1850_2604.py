from numpy import *
from numpy.linalg import *
m=array(eval(input("matriz: ")))
c=m.shape[1]
l=m.shape[0]
for i in range (l):
	print(max(m[i,:]))