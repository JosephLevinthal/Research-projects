from numpy import *
from numpy.linalg import *

trafego=array([[1,-1,0,0],
					[0, 1, -1, 0],
					[0, 0 ,1 ,0],
					[1, 0, 0, 1]])
intersecao=array([50,-120,350,870])
a=dot(inv(trafego), intersecao.T)
print(a)


