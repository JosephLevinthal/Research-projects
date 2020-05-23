from numpy import*
from numpy.linalg import*
m=array(eval(input("matriz: ")))
j=0
for i in range(size(m)):
	for k in range(shape(m)[0]):
		if k+j == shape(m)[0]-1:
			m[k,j]=0
	j=j+1
vet=zeros(shape(m)[0],dtype=float)
for q in range(shape(m)[0]):
	vet[q]= min(m[q,:])
print(min(vet))
		
		