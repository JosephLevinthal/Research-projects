from numpy import* 
from numpy.linalg import*
matriz=array(eval(input("digite a matriz: ")))
l=matriz.shape[0]
c=matriz.shape[1]
prod=0
for i in range(l):
	d=matriz[i,:]
	prod=prod+(d[0]*d[1])/2
print(round(prod/l,2))