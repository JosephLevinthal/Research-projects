from numpy import *
from numpy.linalg import *

mat=array(eval(input("digite a matriz: ")))
l= mat.shape[0]
for i in range(l):
	print(max(mat[i,:]))