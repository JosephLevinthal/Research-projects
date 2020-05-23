from numpy import *
from numpy.linalg import *

vini = array(eval(input("hugug: ")))
l = zeros(shape(vini)[0], dtype=float)
l2 = zeros(shape(vini)[1], dtype=float)
n = 0
n1 = 0
for i in range(size(l)):
	for j in range(7):
		l2[j] = vini[i,j]
	l[i]=max(l2)
for i in range(size(l)):
	print(l[i])