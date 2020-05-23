from numpy import*
from numpy.linalg import*

vetor= array([[1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, 0], [1, 0, 0, 1]])

a = array([50, -120, 350, 870])
a = a.T

b = dot(inv(vetor), a)

print(b)