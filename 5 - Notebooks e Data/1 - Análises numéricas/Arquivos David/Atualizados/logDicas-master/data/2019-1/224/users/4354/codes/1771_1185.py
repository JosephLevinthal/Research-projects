from numpy import *
vetor = array(eval(input("digite o vetor: ")))
i = 0
p = 0
while(i<size(vetor)):
	if(vetor[i]>99):
		print(i)
		p = p + 1
	i = i + 1
print(p)
