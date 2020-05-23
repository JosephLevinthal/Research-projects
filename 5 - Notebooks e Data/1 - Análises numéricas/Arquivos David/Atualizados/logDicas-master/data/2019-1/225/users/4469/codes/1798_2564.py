from numpy import*

v1 = array(eval(input()))
v2 = array(eval(input()))
v3 = zeros(3, dtype = int)

v = 0
e = 0
d = 0

i = 0
while(i < size(v1)):
	if(v1[i] > v2[i]):
		v = v + 1
	elif(v1[i] == v2[i]):
		e = e + 1
	else:
		d = d + 1
	i = i + 1

v3[0] = v
v3[1] = e
v3[2] = d

print(v3)