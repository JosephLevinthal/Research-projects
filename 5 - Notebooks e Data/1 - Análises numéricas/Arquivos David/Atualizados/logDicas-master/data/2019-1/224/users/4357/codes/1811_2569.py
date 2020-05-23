from numpy import*
from math import*
vetor=array(eval(input("digite o numero:")))
a=0
b= sum(vetor)/size(vetor)
for i in vetor:
	a=a+(i-b)**2
d=sqrt(a/(size(vetor)-1))
print(round(d,3))