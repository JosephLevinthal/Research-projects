from numpy import *

v = array(eval(input("Digite: ")))
impar=0
k=0
for i in range(size(v)):
	if not(v[i]%2==0):
		impar+=1
		
x=zeros(impar,dtype=int)
for j in range(size(v)):
	if not(v[j]%2==0):
		x[k]=v[j]
		k+=1
print(x)