from numpy import *
from numpy.linalg import *
mtrz = array(eval(input('digite a matriz: ')))
c = mtrz.shape [1]
l = mtrz.shape [0]
for i in range(l):
	print(max(mtrz[i,:]))
