from numpy.linalg import*
from numpy import*

x=array(eval(input("")))

w=zeros(x.shape[0], dtype=float)
for i in range(x.shape[0]):
	if i in range(x.shape[1]):
		if i==i:
			w[i]+=x[i,i]
print(round(sum(w),2))

