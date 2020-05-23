from numpy import *

m = array(eval(input('Matricula: ')))
v = 0

for i in range(size(m)):
	if m[i]%2!=0:
		v = v+1
k = zeros(v, dtype=int)
t = 0
for i in range(size(m)):
	if m[i]%2!=0:
		k[t] = m[i]
		t = t+1
print(k)