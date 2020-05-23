from numpy import*
from numpy.linalg import*

n  = array(eval(input("Digite um numero natural n: ")))

a = zeros((n,n), dtype=int)
for i in range(n):
		for j in range(n):
			if (i > j):
				a[i,j] = j + 1
			elif	(i <= j):
					a[i,j] = i + 1

print(a)