from numpy import *
v = array(eval(input("")))

nimpar = 0

for i in range(size(v)):
	if(v[i]%2 !=0):
		nimpar = nimpar + 1

n = zeros(nimpar,dtype=int)
r = 0

for j in range(size(v)):
	if(v[j] %2 !=0):
		n[r] = v[j]
		r = r + 1
		
print(n)