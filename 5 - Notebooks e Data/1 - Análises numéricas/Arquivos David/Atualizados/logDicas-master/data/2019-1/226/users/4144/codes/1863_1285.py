from numpy import *
from numpy.linalg import *
a = array(eval(input("digite: ")))
mat = array([
	[4,5,2],
	[3,2,2],
	[2,3,3],
])
k = dot(inv(mat),a.T)

print("grande: ",round(k[0],0))
print("medio: ",round(k[1],0))
print("pequeno: ",round(k[2],0))

if(max(k)==k[0]):
	print("grande")
elif(max(k)==k[1]):
	print("medio")
elif(max(k)==k[2]):
	print("pequeno")