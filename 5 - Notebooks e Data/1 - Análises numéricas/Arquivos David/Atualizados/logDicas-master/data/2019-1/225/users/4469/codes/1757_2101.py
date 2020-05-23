from numpy import*

n = int(input())

if(n > 2):
	v = zeros(n, dtype = int)
	
	v[1] = 1
	i = 2
	while(i < n):
		v[i] = v[i - 1] + v [i - 2]
		i = i + 1
	
	print(v)