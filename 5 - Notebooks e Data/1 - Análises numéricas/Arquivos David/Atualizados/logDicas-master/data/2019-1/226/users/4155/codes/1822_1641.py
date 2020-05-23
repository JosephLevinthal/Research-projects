from numpy import *
v = array(eval(input("v: ")))
b = 0
for i in range(size(v)): 
	if v[i]%3 == 0:
		b = b + 1
print(b)

x = zeros(b, dtype=int)

for i in range(size(v)):
	if v[i]%3 == 0:
		x[i] = v[i] + 1  
print(x)
	