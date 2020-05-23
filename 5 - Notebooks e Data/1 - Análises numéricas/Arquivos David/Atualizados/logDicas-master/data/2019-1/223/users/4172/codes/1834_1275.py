from numpy import*
from numpy.linalg import*

x=array(eval(input("")))

a=zeros(x.shape[0], dtype=int)

for i in range(x.shape[0]):
	a[i]=sum(x[i,:])
	
print(a)