from numpy import*
from numpy.linalg import*

x=array(eval(input("")))

w=zeros(x.shape[0], dtype=int)
a=0
for i in range(x.shape[0]):
	w[i]=min(x[i,:])
	a+=min(x[i,:])

print(round(sum(a)/size(w),2))