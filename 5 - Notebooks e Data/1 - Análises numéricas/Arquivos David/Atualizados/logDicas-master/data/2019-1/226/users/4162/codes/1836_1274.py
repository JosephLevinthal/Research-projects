from numpy import*
from numpy.linalg import*
s=0
n=array(eval(input("insira um numero natural: ")))
mt=zeros((n,n),dtype=int)
for i in range(n):
	for j in range(n):
		mt[i,j]=min(i,j)+1
print(mt)