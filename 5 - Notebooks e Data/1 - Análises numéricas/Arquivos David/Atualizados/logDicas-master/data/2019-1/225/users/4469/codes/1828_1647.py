from numpy import*

v1 = array(eval(input()))

a = 0
for i in v1:
	if(i >= 70):
		a += 1

print(a)

v2 = zeros(a, dtype = int)

j = 0
for i in range(size(v1)):
	if(v1[i] >= 70):
		v2[j] = i
		j += 1

print(v2)