from numpy import *
vetor=array(eval(input("vetor: ")))
p=0
p1=0
s=0
while(p<size(vetor)):
	if(vetor[p]>0):
		s=s+1
	p=p+1
while(p1>0):
	if(vetor[p]<0):
		vetor=vetor-vetor[p]