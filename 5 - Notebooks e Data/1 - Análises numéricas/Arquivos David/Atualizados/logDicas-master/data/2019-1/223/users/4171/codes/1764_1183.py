from numpy import *

v = array(eval(input("vetor v: "))) 

i = 0
r = 0
t = 0
k = 0

while i != size(v):
	if v[i] >= 0:
		
		r+=1
		
	i += 1

x = zeros(r, dtype = int)

while k != size(v):
	if v[k] > 0:
		
		x[t] = v[k]
		
		t += 1
		
	k += 1

print(x)