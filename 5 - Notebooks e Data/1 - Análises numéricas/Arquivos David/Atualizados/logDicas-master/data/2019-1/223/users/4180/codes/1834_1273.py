from numpy import*
from numpy.linalg import*
#matriz do sistema linear
coeficientes=array([[1,-1,0,0],[0,1,-1,0],[0,0,1,0],[1,0,0,1]])

#matriz linha
valores=array([50,-120,350,870])

#matriz coluna
valores=valores.T

#resolucao do sistema de equacoes ineares
solucao=solve(coeficientes,valores)
print(solucao)