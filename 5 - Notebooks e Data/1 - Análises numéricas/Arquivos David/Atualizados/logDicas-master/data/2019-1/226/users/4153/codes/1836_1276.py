from numpy import*
from numpy.linalg import*

m = array(eval(input ("insira: ")))
v = zeros (7,dtype=int)
for i in range (7):
   v [i] = sum(m [:,i])
for x in range (7):
   if (v [x] == max (v)):
      print (x + 1)8