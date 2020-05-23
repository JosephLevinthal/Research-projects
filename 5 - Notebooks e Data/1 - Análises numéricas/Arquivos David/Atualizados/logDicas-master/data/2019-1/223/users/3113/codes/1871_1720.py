from numpy import*
from numpy.linalg import*

matriz=array(eval(input("")))

s=matriz.shape[0]
d=0

for i in range(s):
	if(sum(matriz[i,:])/s>=5):
		d=d+1
f=100/s
r=f*d
print(round(r,2))