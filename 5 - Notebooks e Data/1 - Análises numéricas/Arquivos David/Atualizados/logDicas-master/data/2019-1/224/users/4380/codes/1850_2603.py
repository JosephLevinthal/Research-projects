from numpy import *
from numpy.linalg import *
mat=array(eval(input("matriz: ")))
c= mat.shape[1]
maz=zeros((4,4),dtype=int)
for i in range (c):
	for j in range (c):
		mat[:,j]=sorted(mat[:,j],reverse=True)
print(mat)