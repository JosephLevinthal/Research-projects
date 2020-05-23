from numpy import*
from numpy.linalg import*
a=array(eval(input("sadihL:")))
b=shape(a)[0]
total=zeros(b,dtype=int)

for i in range(b):
	total[i]=sum(a[i,:])
	
print(total)
	