from numpy import *
V = array(eval(input("digite o vetor : ")))
i=0
t=0
while(i<size(V)):
	if(V[i]>99):
		t = t + 1
		print(i)
	i = i + 1
print(t)