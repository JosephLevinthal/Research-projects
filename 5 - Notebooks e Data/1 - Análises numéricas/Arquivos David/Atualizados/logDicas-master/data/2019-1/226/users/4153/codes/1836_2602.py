from numpy import *
from numpy.linalg import *

g = array(eval(input("Insira a qtd de alimento: ")))

a = array ([[2, 1, 4],
				[1, 2, 0],
				[2, 3, 2]])
t = array (dot (inv (a),g.T))
print ("estafilococo:",round (t [0],1))
print ("salmonela:",round (t [1],1))
print ("coli:",round (t [2],1))
m = min (t)
for i in range (size (t)):
   if (t [i] == m):
      m = i
if (m == 0):
   print ("estafilococo")
elif (m==1):
   print ("salmonela")
elif (m == 2):
   print ("coli")