from numpy.linalg import*
from numpy import*

l1 = int(input("linha: "))
c1 = int(input("coluna: "))
i = 0

a = zeros((l1, c1), dtype=int)

while(i < l1 ):
	a[i,:] = input("").split(',')
	i = i + 1
print(a)
print(l1*c1)