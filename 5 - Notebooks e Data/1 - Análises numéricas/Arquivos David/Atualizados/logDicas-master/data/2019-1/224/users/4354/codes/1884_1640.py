from numpy import *
v = array(eval(input("digite o vetor: ")))
e = 0
for i in range(size(v)):
	if(v[i]%5 == 0):
		e = e + 1
z = zeros(e,dtype = int)
p = 0
for j in range(size(v)):
	if(v[j] % 5 == 0):
		z[p] = j
		p = p + 1
print(e)
print(z)
		