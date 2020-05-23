from numpy.linalg import*
from numpy import*

x=array(eval(input("")))


for i in range(shape(x)[0]):
	for j in range(shape(x)[0]):
		if x[i,j]==x[j,i]:
			a="SIMETRICA"
for i in range(x.shape[0]):
	for i in range(x.shape[0]):
		if x[i,j]!=x[j,i]:
			a="ASSIMETRICA"
print(a)
