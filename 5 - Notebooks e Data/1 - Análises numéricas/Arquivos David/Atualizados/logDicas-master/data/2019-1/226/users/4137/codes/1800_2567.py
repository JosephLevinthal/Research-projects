from numpy import*

n = int(input("Um numero:"))
d = "*"
s = zeros(n, dtype=int)
for i in range(size(s)):
	d = "*"*n
	n = n-1
	print(d)
for i in range(size(s)+1):
	d = "*"*n
	n = n+1
	print(d)