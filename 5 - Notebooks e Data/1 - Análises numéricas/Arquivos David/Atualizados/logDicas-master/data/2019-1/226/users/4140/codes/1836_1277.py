from numpy import *
from numpy.linalg import *
i=int(input())
j=int(input())
mat=array([[0,2,11,6,15,11,1],[2,0,7,12,4,2,15],[11,7,0,11,8,3,13],[6,12,11,0,10,2,1],[15,4,8,10,0,5,13],[11,2,3,2,5,0,14],[1,15,13,1,13,14,0]])
if i==111:
	i=0
elif i==222:
	i=1
elif i==333:
	i=2
elif i==444:
	i=3
elif i==555:
	i=4
elif i==666:
	i=5
elif i==777:
	i=6
if j==111:
	j=0
elif j==222:
	j=1
elif j==333:
	j=2
elif j==444:
	j=3
elif j==555:
	j=4
elif j==666:
	j=5
elif j==777:
	j=6
print(mat[i,j])

