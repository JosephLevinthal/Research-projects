from numpy import *
from numpy.linalg import *

f = array([[2, 1, 4], [1 ,2  , 0], [2 ,3  ,2  ]])
v = array(eval(input())).T

p = dot(inv(f) ,v )

print("estafilococo: ", round(p[0], 1))
print("salmonela: ", round(p[1], 1))
print("coli: ", round(p[2], 1))

if p[0] == min(p):
    print("estafilococo")
elif p[1] == min(p):
    print("salmonela")
else:
    print("coli")
