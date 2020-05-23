from numpy import *
vetor = array(eval(input("digite os numeros inteiros: ")))
i = 0
z = zeros(size(vetor),dtype = int)
while(i<size(vetor)):
	if(vetor[i]%2 == 0):
		z[i] = vetor[i]
	else:
		z[i] = 0
	i = i + 1
print(z)