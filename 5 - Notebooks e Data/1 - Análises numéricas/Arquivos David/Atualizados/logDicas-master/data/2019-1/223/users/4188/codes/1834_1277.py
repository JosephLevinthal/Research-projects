from numpy import *
from numpy.linalg import *
a = int(input("coluna: "))
b = int(input("linha: "))
tabela = array([[0, 2,11,6,15,11,1], 
					 [2, 0,7,12,4,2,45],
					 [11,7,0,11,8,3, 13],
					 [6,12,11,0,10,2,1],
					 [15,4,8,10,0,5,13],
					 [11,2,3,2,5,0,14],
					 [1,15,13,1,13,14,0]])
c = tabela[(b//100)-1,(a//100)-1]
print(c)