from numpy import*
from numpy.linalg import *
v = array([[0,2,11,6,15,11,1],
		[2,0,7,12,4,2, 15],
		[11,7,0,11,8,3,13],
		[6,12,11,0,10,2,1],
		[15,4,8,10,0,5,13],
		[11,2,3,2,5,0, 14],
		[1,15,13,1,13,14,0]])
c1 = int(input("Cidade 1: "))
c2 = int(input("Cidade 2: "))
x = (c1//111)-1
y = (c2//111)-1			
print(v[x,y])