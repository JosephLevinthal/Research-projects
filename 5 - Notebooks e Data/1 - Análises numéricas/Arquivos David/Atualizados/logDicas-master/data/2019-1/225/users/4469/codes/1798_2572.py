from numpy import*

v1 = array(eval(input()))

v2 = array([], dtype = int)

for i in v1:
	if(i % 2 != 0):
		v2 = append(v2, [i])

print(v2)