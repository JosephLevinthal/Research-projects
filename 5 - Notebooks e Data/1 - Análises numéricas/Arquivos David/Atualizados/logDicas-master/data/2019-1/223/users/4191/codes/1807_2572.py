from numpy import *

vetor=array(eval(input("...")))
impar=0
for i in range(size(vetor)):
	if(vetor[i] % 2 != 0):
		impar=impar+1
		
v=zeros(impar, dtype=int)		
d=0
for i in range(size(vetor)):
	if(vetor[i]%2!=0):
		v[d]=vetor[i]
		d=d+1
print(v)		