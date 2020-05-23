from numpy import *
vetor = array(eval(input("vator:")))
a = zeros(4,dtype=int)
for i in range(size(vetor)):
	if(vetor[i]==1):
		a[0]= a[0] + 1
	if(vetor[i]==2):
		a[1]= a[1] + 1
	if(vetor[i]==3):
		a[2]= a[2] + 1
	if(vetor[i]==4):
		a[3]= a[3] + 1
print(a)