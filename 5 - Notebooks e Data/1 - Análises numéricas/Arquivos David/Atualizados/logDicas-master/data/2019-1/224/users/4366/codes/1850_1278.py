from numpy import *
from numpy.linalg import *
cidade1=input("digite a cidade 1: ")
mat=array([[0,2,11,6,15,11,1],
			  [2,0,7,12,4,2,15],
			  [11,7,0,11,8,3,13],
			  [6,12,11,0,10,2,1],
			  [15,4,8,10,0,5,13],
			  [11,2,3,2,5,0,14],
			  [1,15,13,1,13,14,0]])
t=0
i=0
j=1
while(cidade1 != "-1"):
	if(i!=j):
		i=int(cidade1[0]) -1
		cidade1= input("digite novamente: ")
	if(cidade1 != "-1"):
		j=int(cidade1[0]) -1
		t=t+ mat[i,j]
		cidade1=input("digite novamente: ")
		i=j
print(t)






