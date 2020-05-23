from numpy import*

n = int(input())
m = zeros((n,n), dtype = int)
for i in range(n):
	s = input()
	m[i,:] = s.split(" ")

s1 = s2 = 0
for i in range(n):
	for j in range(n):
		if(i == j):
			s1 += m[i,j]
		if(i + j == n - 1):
			s2 += m[i,j]

print(s1-s2)