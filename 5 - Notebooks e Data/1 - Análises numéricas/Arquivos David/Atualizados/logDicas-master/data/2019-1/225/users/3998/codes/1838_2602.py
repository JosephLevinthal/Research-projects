from numpy import *
from numpy.linalg import *

mg= array(eval(input(": ")))
e = array([[2,1,4],[1,2,0],[2,3,2]])


q = dot(inv(e),mg.T)

print("estafilococo: ", round(q[0], 1))
print("salmonela: ", round(q[1], 1))
print("coli: ", round(q[2], 1))

if q[0] == min(q):
    print("estafilococo")
elif q[1] == min(q):
    print("salmonela")
else:
    print("coli")