from numpy import *
n = int(input(""))
v = array([0]*n)
v[0] = 0
v[1] = 1
for i in range(2,n):
	v[i]=v[i-1]+v[i-2]
print(v)