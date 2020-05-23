from numpy import *
from numpy.linalg import*

coefi = array([[1, -1, 0, 0],
					[0, 1, -1, 0],
					[0, 0, 1, 0],
					[1, 0, 0, 1]])
result = array([50, -120, 350, 870])

vs = solve(coefi, result)
print(vs)