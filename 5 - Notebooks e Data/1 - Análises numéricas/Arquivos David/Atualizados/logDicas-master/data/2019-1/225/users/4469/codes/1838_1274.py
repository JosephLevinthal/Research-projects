from numpy import *

n = int(input())
m = ones((n, n), dtype = int)
j = 1
k = 2

for i in range(1,n):
	while(j < n):
		m[i, j] = i + 1
		j += 1
	j = k
	k += 1
	
i = 1
k = 2
for j in range(1, n):
	while(i < n):
		m[i, j] = j + 1
		i += 1
	i = k
	k += 1

print(m)