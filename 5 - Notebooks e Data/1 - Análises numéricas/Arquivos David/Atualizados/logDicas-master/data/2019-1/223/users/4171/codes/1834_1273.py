from numpy import *
from numpy.linalg import *

a = array([[1, -1, 0, 0], [0, 1 , -1, 0], [0, 0, 1, 0], [1, 0, 0, 1]])
b = array([50, -120, 350, 870])
c = dot(inv(a),b.T)
print(c)