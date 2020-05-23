from numpy import*
from numpy.linalg import*

x = array ([[1,-1,0,0],[0,1,-1,0],[0,0,1,0],[1,0,0,1]])

valores = array([50,-120,350,870])
valores = valores.T

solucao = solve(x, valores)
print(solucao)