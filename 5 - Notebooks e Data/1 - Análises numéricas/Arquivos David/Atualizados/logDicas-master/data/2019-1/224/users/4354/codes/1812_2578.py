from numpy import *
v = array(eval(input("digite o vetor forcas: ")))
p = 0
for i in v:
	if(i % 2 == 0):
		p = p + 1
z = zeros(p,dtype = int)
zpos = 0
for i2 in v:
	if(i2 % 2 == 0):
		z[zpos] = i2
		zpos = zpos + 1
print(z)
	
