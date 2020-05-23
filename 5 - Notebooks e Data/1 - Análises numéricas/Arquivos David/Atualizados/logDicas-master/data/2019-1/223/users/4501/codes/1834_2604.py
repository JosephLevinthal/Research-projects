from numpy import*
from numpy.linalg import *
a=array(eval(input("vetor: ")))
for i in range(a.shape[0]):
	print(max(a[i,:]))