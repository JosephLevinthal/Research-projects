from numpy import*
from numpy.linalg import *
vetor = array(eval(input("vetor: ")))
a = array([[2,1,2],[1,2,3],[4,0,2]])
a = a.T
b = dot(inv(a),vetor)
print("estafilococo: ", round(b[0], 1))
print("salmonela: ", round(b[1], 1))
print("coli: ", round(b[2], 1))

if b[0] == min(b):
    print("estafilococo")
elif b[1] == min(b):
    print("salmonela")
else:
    print("coli")


