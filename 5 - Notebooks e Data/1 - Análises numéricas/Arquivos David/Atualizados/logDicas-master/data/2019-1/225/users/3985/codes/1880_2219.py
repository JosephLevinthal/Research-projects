from numpy import*
from numpy.linalg import*

a=array(eval(input()))
b=0
for i in range(size(a)):
	for j in range(size(a)):
		if(b<size(a)):
			c=sum(a[i:j])
		b+=1
print(c)