from numpy import *
from numpy.linalg import *
mat = array(eval(input("digite a matriz :")))
n = int(input("digite: "))
c = mat.shape[1]
s = sum(mat[n,:])
med = s/c
print(round(med,2))