from numpy import *
from numpy.linalg import *

f = array([[1,-1,0,0],[0,1,-1,0],[0,0,1,0],[1,0,0,1]])

fluxo = array([50,-120,350,870])
fluxo = fluxo.T

x = dot(inv(f),fluxo)

print(x)