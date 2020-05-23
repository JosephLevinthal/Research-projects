from numpy import*
from numpy.linalg import*
a=int(input())
prin=0
sec=0
mat=zeros((a,a),dtype=int)
for i in range(a):
	b=(input())
	b=b.split(' ')
	
	for j in range(size(b)):
		mat[i,j]=b[j]
for k in range(a):
	prin=mat[k,k]+prin
for w in range(a) :
	sec=mat[-1-w,-1-w]+sec
resu=prin-sec
print(resu)