from numpy import*
from numpy.linalg import*
a = array(eval(input()))
b = int(input())
w = 0
f = shape(a)[0]
g = shape(a)[1]
for i in range(g):
	w += a[i,b]
x = w/f
if x >= 5.0:
	print("PASSOU")
else:
	print("REPROVOU")