
from numpy import *
from numpy.linalg import *

a = array([50 , -120 , 350 , 870])

rua = array([[1,-1,0,0], [0,1,-1,0], [0,0,1,0],[1,0,0,1]])

x  = dot(inv(rua), a.T)
aa = inv(rua)
ruaa = a.T
print(x)
print(aa)
print(ruaa)
