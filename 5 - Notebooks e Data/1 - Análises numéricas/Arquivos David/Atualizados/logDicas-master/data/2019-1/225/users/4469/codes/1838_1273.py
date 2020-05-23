from numpy import *
from numpy.linalg import *

m = array([[1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, 0], [1, 0, 0, 1]])
v = array([50, -120, 350, 870])

x = dot(inv(m), v.T)

print(x)