from numpy import *
from numpy.linalg import *
m=array(eval(input("matriz: ")))
c=m.shape[1]
z=zeros(c,dtype=int)
for j in range (c):
	z[j]=sum(m[:,j])
for n in range (size(z)):
	if(z[n]==max(z)):
		print(n+1)