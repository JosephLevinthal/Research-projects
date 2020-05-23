from numpy import *
from numpy.linalg import *

x = array(eval(input()))
a = shape(x)[1]
y = int(input())
h = 0

for j in range(a):
	if j == y :
		h = (x[j,:])
f = sum(h)/a
if f >= 5:
	print("PASSOU")
else:
	print("REPROVOU")