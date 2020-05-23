from numpy import *
from numpy.linalg import *
mte = array(eval(input("digite uma matriz 4x4: ")))
aux = zeros(4, dtype=int)
for j in range(4):
	mte[:,j] = sorted(mte[:,j], reverse=True)
print(mte)	
		

