from numpy import *
from numpy.linalg import *

m = array (eval (input ("insira:")))
v = zeros (7,dtype=int)
for i in range (shape(m)[0]):
   v = m [i,:]
   print (max (v))