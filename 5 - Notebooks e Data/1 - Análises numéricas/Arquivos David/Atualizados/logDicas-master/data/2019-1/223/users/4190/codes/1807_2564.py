from numpy import *

v1 = array(eval(input('Gols: ')))
v2 = array(eval(input('Gols adversarios: ')))
v3 = zeros(3, dtype=int)

for i in range(size(v1)):
	if (v1[i]>v2[i]):
		v3[0] = v3[0]+1
	if (v1[i]==v2[i]):
		v3[1] = v3[1]+1
	if (v1[i]<v2[i]):
		v3[2] = v3[2]+1
print(v3)