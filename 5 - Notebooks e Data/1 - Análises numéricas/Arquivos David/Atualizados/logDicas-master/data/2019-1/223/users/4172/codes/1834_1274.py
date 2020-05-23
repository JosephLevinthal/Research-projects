from numpy.linalg import*
from numpy import*

	
x=array(eval(input("")))
print(x)

w=zeros((x,x), dtype=int)

for i in range(0,x):
	for j in range(0,x):
		w[i,j]=min(i,j)+1
print(w)