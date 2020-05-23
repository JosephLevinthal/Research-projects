from numpy import*
from numpy.linalg import*
x=array(eval(input("hora do riso: ")))
w= shape(x)[1]
h= shape(x)[0]
k = zeros(7,dtype=int)
for i in range(7):
	k[i]=sum(x[:,i])
for q in range(size(k)):
	if(k[q]==max(k)):
		print(q+1)
	