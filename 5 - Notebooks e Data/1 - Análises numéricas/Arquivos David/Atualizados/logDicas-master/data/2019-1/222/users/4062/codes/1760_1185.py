from numpy import *

v = array(eval(input("Glicose: ")), dtype=int)

for i in range(size(v)):
	if (v[i] > 99):
		print(i)

a = 0
for p in range(size(v)):
	if (v[p] > 99):
		a = a + 1
		
print(a)