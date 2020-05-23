from numpy import *
from numpy.linalg import *

mg=array(eval(input()))

consumo=array([[2,1,4],[1,2,0], [2,3,2]], dtype=float)
quantidade=dot(inv(consumo),mg)

print("estafilococo: ", round(quantidade[0], 1))
print("salmonela: ", round(quantidade[1], 1))
print("coli: ", round(quantidade[2], 1))

if quantidade[0] == min(quantidade):
    print("estafilococo")
elif quantidade[1] == min(quantidade):
    print("salmonela")
else:
    print("coli")
