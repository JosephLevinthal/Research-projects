from numpy import *

n = int(input("Numero: "))
m = zeros((n, n), dtype=int)

for i in range(n):
	for j in range(n):
		if i > j:
			m[i, j] = j+1
		elif i <= j:
			m[i, j] = i+1
	
print(m)