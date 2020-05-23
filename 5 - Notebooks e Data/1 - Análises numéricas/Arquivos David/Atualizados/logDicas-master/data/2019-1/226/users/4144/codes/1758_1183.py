from numpy import *
n = array(eval(input("digite o vetor: ")))
i = 0
p=0
while(i<size(n)):
	if(n[i]>=0):
		p = p +1
	i = i +1
r = zeros(p, dtype= int)
a = 0
b = 0
while(a<size(n)):
	if(n[a]>0):
		r[b] = n[a]
		b = b +1
	a = a+1
print(r)