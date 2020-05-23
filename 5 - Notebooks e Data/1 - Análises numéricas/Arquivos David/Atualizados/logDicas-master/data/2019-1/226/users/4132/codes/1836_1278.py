from numpy import *
from numpy.linalg import *         



mat = array ([[0,2,11,6,15,11,1],
				  [2,0,7,12,4,2,15],
				  [11,7,0,11,8,3,13],
				  [6,12,11,0,10,2,1],
				  [15,4,8,10,0,5,13],
				  [11,2,3,2,5,0,14],
				  [1,15,13,1,13,14,0]])

soma=0
a=0
b=0
aux=111
vet= zeros(7,dtype=int)
for i in range(7):
	vet[i]=aux
	aux+=111
	
n = int(input("digite 1: "))
n2=1
while(n2!=-1):
	n2 = int(input("digite 1: "))
	
	for i in range(7):
		if(n == vet[i]):
			a = i
		if(n2 == vet[i]):
			b=i
	soma+=mat[a,b]
	a=b
	n=n2
print(soma)

