from numpy import*
from numpy.linalg import*

m = array(eval(input("digite algo: ")))
vet = zeros(shape(m)[1],dtype=int)
for i in range(4):
	for j in range(4):
		vet[j] = m[j,i]
	vet = sorted(vet,reverse=True)
	for k in range(4):
		m[k,i]=vet[k]
print(m)