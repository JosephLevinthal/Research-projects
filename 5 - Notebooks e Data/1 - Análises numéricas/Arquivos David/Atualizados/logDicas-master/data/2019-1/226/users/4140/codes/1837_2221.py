from numpy import*
from numpy.linalg import*
mat=array(eval(input()))
a=shape(mat)[0]
v=zeros(a)
for i in range(a):
	v[i]=min(mat[i,:])
resu=sum(v)/size(v)
print(round(resu,2))