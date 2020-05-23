from numpy import *
from numpy.linalg import *

matriz = array([[1,-1,0,0],[0,1,-1,0],[0,0,1,0],[1,0,0,1]])

resultado = array([50,-120,350,870])
resultado = resultado.T

vetor = dot(inv(matriz),resultado)
vetor = vetor.T

print(vetor)