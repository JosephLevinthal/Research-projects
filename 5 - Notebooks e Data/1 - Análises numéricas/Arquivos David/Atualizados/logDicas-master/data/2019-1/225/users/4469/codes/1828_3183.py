from numpy import*

v1 = array(eval(input()), dtype = int)

v2 = zeros(size(v1), dtype = int)
j = 0
for i in range(size(v1) - 1, -1, -1):
	v2[j] = v1[i]
	j = j + 1

for i in range(size(v2)):
	v1[i] = v2[i]

print(v1)