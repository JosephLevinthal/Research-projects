from numpy import *
vetor=array(eval(input("digite o vetor")))
i=0
t=0
while(i<size(vetor)):
	if(vetor[i]>99):
		print(i)
		t=t+1
	else:
		t=t+0
	i=i+1
print(t)
		

