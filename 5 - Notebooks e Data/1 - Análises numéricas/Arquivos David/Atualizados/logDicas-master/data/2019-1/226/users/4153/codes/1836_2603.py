from numpy import*
from numpy.linalg import *

m = array (eval (input ("insira:")))

v1 = array (m [:,0])
v2 = array (m [:,1])
v3 = array (m [:,2])
v4 = array (m [:,3])
v1 = sorted(v1, reverse=True)
v2 = sorted(v2, reverse=True)
v3 = sorted(v3, reverse=True)
v4 = sorted(v4, reverse=True)

r = array ([v1,v2,v3,v4])

print (r.T)