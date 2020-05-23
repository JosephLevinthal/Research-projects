from numpy import *
from numpy.linalg import *
m = int(input("v: "))
m3 = int(input("q: "))
mt = array([[0,2,11,6,15,11,1], 
				[2,0,7,12,4,2,15],
				[11,7,0,11,8,3,13], 
				[6,12,11,0,10,2,1], 
				[15,4,8,10,0,5,13], 
				[11,2,3,2,5,0,14], 
				[1,15,13,1,13,14,0]])
y = 1
p = 0
ax = 111
vt = zeros(7,dtype = int)
for i in range(7):
	vt[i] = ax
	ax += 111
for i in range(7):
	if(m == vt[i]):
		y = i
	if(m3 == vt[i]):
		p = i
print(mt[y,p])