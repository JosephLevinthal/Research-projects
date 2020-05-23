from numpy import*
from numpy.linalg import*

v = array([50, -120, 350, 870])
v = v.T

eq = array([
	[1, -1, 0, 0],
	[0, 1, -1, 0],
	[0, 0, 1, 0],
	[1, 0, 0, 1]])
v = dot(inv(eq), v.T)
print(v)