from numpy import*
from numpy.linalg import*

saida = array([50,-120,350,870])
saida = saida.T

eq = array([[1,-1,0,0],[0,1,-1,0],[0,0,1,0],[1,0,0,1]])

jj= dot(inv(eq), saida)

print(jj)