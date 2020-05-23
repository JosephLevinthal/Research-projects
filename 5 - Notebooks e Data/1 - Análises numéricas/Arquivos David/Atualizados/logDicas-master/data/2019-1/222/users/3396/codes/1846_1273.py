from numpy import *
from numpy.linalg import *

coeficiente = array([[1, -1, 0, 0 ], [ 0, 1, -1, 0], [ 0, 0, 1, 0], [1, 0, 0, 1]])

valor = array([50, -120, 350, 870])

solucao = dot(inv(coeficiente), valor.T)

print(solucao)
