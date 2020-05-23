from numpy import*

v = array(eval(input()))

i = 0
n = 0

while(i < size(v)):
	if(v[i] >= 0):
		n = n + 1
	
	i = i + 1

i = 0
j = 0
v2 = zeros(n, dtype = int)

while(i < size(v)):
	if(v[i] >= 0):
		v2[j] = v[i]
		j = j + 1
	
	i = i + 1

print(v2)