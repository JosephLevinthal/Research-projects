from numpy import*
from numpy.linalg import *

flux=array([[1,-1,0,0],[0,1,-1,0],[0,0,1,0],[1,0,0,1]])

res=array([50,-120,350,870])
res=res.T

coef=dot(inv(flux),res)


print(coef)