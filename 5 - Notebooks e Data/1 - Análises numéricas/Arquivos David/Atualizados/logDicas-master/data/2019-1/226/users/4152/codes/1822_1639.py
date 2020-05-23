from numpy import *
v = array(eval(input("v: ")))
par = 0
a = 0
for i in range(size(v)):
	if (v[i] % 2 == 0):
		par = par + 1

vpar = zeros(par, dtype=int)
for z in range(size(v)):
	if (v[z] % 2 == 0):
		vpar[a] = z
		a = a + 1 
print(par)
print(vpar)