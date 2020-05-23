from numpy import *
from numpy.linalg import *

matriz = array([[1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, 0], [1, 0, 0, 1]])
r = array([50, -120, 350, 870])

r = r.T
M = dot(inv(matriz), r)
print(M)