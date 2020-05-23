from numpy import *
from numpy.linalg import *

t = array([[0,2,11,6,15,11,1],
			 [2,0,7,12,4,2,15],
			 [11,7,0,11,8,3,13],
			 [6,12,11,0,10,2,1],
			 [15,4,8,10,0,5,13],
			 [11,2,3,2,5,0,14],
			 [1,15,13,1,13,14,0]])

x = int(input())
y = int(input())
h = 0

while x != -1 and y != -1:
	a = (x//100) -1
	b = (y//100) -1
	h = t[a,b] + h
	x = y
	y = int(input())
print(h)