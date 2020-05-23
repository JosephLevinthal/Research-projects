from numpy import *

v = array(eval(input("Matriculas: ")), dtype=int)
n = 0

for i in range(size(v)):
	if (v[i]%2 != 0):
		n = n + 1
		
s = 0
z = zeros(n, dtype=int)
for i in range(size(v)):
	if (v[i]%2 != 0):
		z[s] = v[i]
		s = s + 1

print(z)