from numpy import*
from numpy.linalg import*
#definimos a entrada da matriz de produtos:
m=array(eval(input("matriz de produtos: ")))
#matriz com total de compras:
b=shape(m)[0]
c=shape(m)[1]
vt=zeros(b, dtype=float)
for i in range(b):
	for j in range(c-1):	
		vt[i]=m[i,j]*m[i,j+1]
total=sum(vt)
print(round(total, 2))
