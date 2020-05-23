from numpy import *
v = array(eval(input('digite o vetor de matriculas: ')))
i = 0
for pos in v:
	if(pos % 2 != 0):
		i = i + 1
z = zeros(i,dtype = int)
imp = 0
for pos2 in v:
	if(pos2 % 2 != 0):
		z[imp] = pos2
		imp = imp + 1
print(z)
