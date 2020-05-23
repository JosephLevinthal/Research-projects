from numpy import *
vetor1 = array(eval(input()))
vetor2 = array(eval(input()))
i = 0

novovet = zeros(size(vetor1), dtype=int)
while(i<size(vetor1)):
	novovet[i] = vetor1[i] - vetor2[i]
	if(max(novovet)==novovet[i]):
		maior = i+1
	i = i +1
	

print(maior)
	