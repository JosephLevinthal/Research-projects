from numpy import*
from numpy.linalg import*
matriz=array(eval(input("digite o numero:")))
b=matriz.shape[0]
soma=0
e=0
for i in range(b):
	soma=matriz[i,0]*matriz[i,1]
	e=e+soma
media=e/b
print(round(media,2))