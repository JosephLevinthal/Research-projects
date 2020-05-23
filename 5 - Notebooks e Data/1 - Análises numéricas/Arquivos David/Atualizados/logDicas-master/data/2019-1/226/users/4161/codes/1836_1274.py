from numpy import*
from numpy.linalg import*
n = int(input("n: "))
m = ones((n,n),dtype=int)

for x in range(n):
	for y in range(n):
		if (x<y):
			m[x,y] = x + 1
		elif (y>x):
			m[x,y] = y + 1
		else:
			m[x,y] = y + 1	
print(m)