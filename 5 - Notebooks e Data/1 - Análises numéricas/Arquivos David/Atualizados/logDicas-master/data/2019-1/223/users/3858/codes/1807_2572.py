from numpy import *

v = array(eval(input()))
i = 0
for x in range (size(v)):
	if(v[x]%2 == 0):
		i = i +1
v2 = zeros(i, dtype=int)
a = 0
for x in range (size(v)):
	if(v[x] % 2 == 0):
		v2[a]=v[x]
		a=a+1
		
