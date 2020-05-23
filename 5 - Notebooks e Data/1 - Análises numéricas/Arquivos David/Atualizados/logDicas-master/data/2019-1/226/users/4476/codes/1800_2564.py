from numpy import *
v1 = array(eval(input("digite: ")))
v2 = array(eval(input("digite: ")))

v3 = zeros(3, dtype=int)

for i in range(size(v1)) and range(size(v2)):
	if v1[i] > v2[i]:
		v3[0] = v3[0] + 1
	elif v1[i] == v2[i]:
		v3[1] = v3[1] + 1
	elif v2[i] > v1[i]:
		v3[2] = v3[2] + 1
print(v3)