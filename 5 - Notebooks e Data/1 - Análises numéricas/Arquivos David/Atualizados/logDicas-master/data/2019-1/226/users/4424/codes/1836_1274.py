from numpy import *
from numpy.linalg import *

x=int(input(":"))
mat=zeros((x,x),dtype=int)

mat=ones((x,x),dtype=int)
n=zeros((x,x),dtype=int)

for i in range(x):
	for j in range(x):
		n[i,j]=min(i,j)+1
print(n)