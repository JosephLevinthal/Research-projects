from numpy import *
from numpy.linalg import *

coeficientes = array([[1,-1,0,0], [0,1,-1,0], [0,0,1,0], [1,0,0,1]])

#linha da matriz
valores = array([50, -120, 350, 870])

#coluna da matriz
valores = valores.T

solucao = solve(coeficientes, valores)

print(solucao)
