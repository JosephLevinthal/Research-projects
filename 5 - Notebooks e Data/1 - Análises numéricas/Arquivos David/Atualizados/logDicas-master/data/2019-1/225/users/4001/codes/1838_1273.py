from numpy import*
from numpy.linalg import*
z = zeros(4, dtype=float)
x = array([[1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, 0], [1, 0, 0, 1]])
v = array([50, -120, 350, 870])
v = v.T
V = dot(inv(x), v)

print(V)