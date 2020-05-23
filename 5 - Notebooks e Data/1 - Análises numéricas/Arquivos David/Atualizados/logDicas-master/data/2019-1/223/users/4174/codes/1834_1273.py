from numpy import *
from numpy.linalg import *

quantidade = array([[1,-1,0,0],[0,1,-1,0],[0,0,1,0],[1,0,0,1]])

valor = array([50,-120,350,870])

valor = valor.T

vetor = solve((quantidade),valor)

print(vetor)
