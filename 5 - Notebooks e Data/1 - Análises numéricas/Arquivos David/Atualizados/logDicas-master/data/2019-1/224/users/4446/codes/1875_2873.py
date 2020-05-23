from numpy import *
from numpy.linalg import *

mat=array(eval(input("digite a matriz: ")))
soma=0

l=mat.shape[0]
for i in range(l):
	prod=mat[i,0]*mat[i,1]
	soma=soma+prod
media=soma/l
print(round(media, 2))