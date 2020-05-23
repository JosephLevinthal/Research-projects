from numpy import *
from numpy.linalg import *
a=int(input("linha: "))
b=int(input("coluna: "))
alvo=array ([[0,2,2,2,0],
	        [2,5,8,5,2],
	        [2,8,16,8,2],
	        [2,5,8,5,2],
	        [0,2,2,2,0]])
c = alvo[a - 1, b -1]
print(c)