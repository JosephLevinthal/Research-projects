from numpy import *
from numpy.linalg import * 
coeficientes = array ([[1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, 0], [1, 0, 0, 1]])
valores = array([50, -120, 350, 870])
valores = valores.T
solucao = solve(coeficientes, valores)
print(solucao)