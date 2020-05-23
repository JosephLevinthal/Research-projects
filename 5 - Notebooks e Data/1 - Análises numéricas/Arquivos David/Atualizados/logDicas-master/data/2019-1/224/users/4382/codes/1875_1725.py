from numpy import *
from numpy.linalg import *
mat = array(eval(input("digite a matriz:")))
B = 0
L = 0
s = 0
for i in range (shape(mat)[0]):
	for j in range (shape(mat)[1]):
		if(mat[i,j]== "B"):
			s = s + 1
print(s)
	
