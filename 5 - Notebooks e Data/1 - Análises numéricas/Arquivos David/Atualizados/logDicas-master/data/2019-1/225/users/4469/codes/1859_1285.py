from numpy import*
from numpy.linalg import*

v = array(eval(input())).T

m = array([[4, 5, 2], [3, 2, 2], [2, 3, 3]])

p = dot(inv(m), v)

print("grande:", round(p[0], 0))
print("medio:", round(p[1], 0))
print("pequeno:", round(p[2], 0))

if(max(p) == p[0]):
	print("grande")
elif(max(p) == p[1]):
	print("medio")
else:
	print("pequeno")