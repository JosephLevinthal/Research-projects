from numpy import *
from numpy.linalg import *
c1=input("cidade 1: ")
mat= array([[0,2,11,6,15,11,1],
				[2,0,7,12,4,2,15],
				[11,7,0,11,8,3,13],
				[6,12,11,0,10,2,1],
				[15,4,8,10,0,5,13],
				[11,2,3,2,5,0,14],
				[1,15,13,1,13,14,0]])
t=0
i=0
j=1
while(c1!="-1"):
	if(i!=j):
		i=int(c1[0])-1
		c1=input("digitar dnv: ")
	if(c1!="-1"):
		j=int(c1[0])-1
		t=t+mat[i,j]
		c1=input("digitar dnv: ")
		i=j
print(t)