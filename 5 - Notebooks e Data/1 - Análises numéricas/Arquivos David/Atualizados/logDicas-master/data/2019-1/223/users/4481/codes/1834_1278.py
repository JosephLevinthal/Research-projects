from numpy import * 
from numpy.linalg import *
tabela = array([[0, 2,11,6,15,11,1], 
					 [2, 0,7,12,4,2,15],
					 [11,7,0,11,8,3, 13],
					 [6,12,11,0,10,2,1],
					 [15,4,8,10,0,5,13],
					 [11,2,3,2,5,0,14],
					 [1,15,13,1,13,14,0]])
a = int(input("digite: "))
c=int(input("digite: "))
b = 0
while(c != -1):
	
	b = tabela[(a//100)-1, (c//100)-1] + b
	a = c
	c=int(input("digite: "))

print(b)